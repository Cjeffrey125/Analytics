from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from project.forms import SignUpForm, AddApplicantForm, ExportForm, ApplicantUploadForm
from .models import CollegeStudentApplication
from django.db.models import Count
from django.http import HttpResponse
import csv

import pandas as pd
from import_export import resources

class CollegeStudentApplicationResource(resources.ModelResource):
    class Meta:
        model = CollegeStudentApplication
        import_id_fields = ('Control Number',)

#import ----------------------------------------------------------------------------------------------------------------------------------
#problem fk nan&update
def import_excel(request):
    if request.method == 'POST':
        form = ApplicantUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file, na_values=["N/A", "-", "Not Available"])
            applicant_count = 0

            for index, row in df.iterrows():
                applicant = CollegeStudentApplication(
                    control_number=row['Control Number'],
                    last_name=row['Surname'],
                    first_name=row['Firstname'],
                    middle_name=row['Middlename'],
                    address=row['Address'],
                    gender=row['Gender'],
                    date_of_birth=row['Date of Birth'],
                    place_of_birth=row['Place of Birth'],
                    contact_no=row['Contact No.'],
                    email_address=row['Email Address'],
                    school=row['Preferred School'],
                    course=row['Desired Course'],
                    gwa=row['GWA'],
                    rank=row['Rank'],
                    
                    jhs=row['JHS'],
                    jhs_address=row['JHS Address'],
                    jhs_educational_provider=row['JHS Education Provider'],

                    shs=row['SHS'],
                    shs_address=row['SHS Address'],
                    shs_educational_provider=row['SHS Education Provider'],

                    father_name=row['Father Name'],
                    father_voter_status=row['Father Voter Status'],
                    father_educational_attainment=row['Father Educational Attainment'],
                    father_employer=row['Father Employer'],
                    father_occupation=row['Father Occupation'],

                    mother_name=row['Mother Name'],
                    mother_voter_status=row['Mother Voter Status'],
                    mother_educational_attainment=row['Mother Educational Attainment'],
                    mother_employer=row['Mother Employer'],
                    mother_occupation=row['Mother Occupation'],

                    guardian_name=row['Legal Guardian'],
                    guardian_voter_status=row['Guardian Voter Status'],
                    guardian_educational_attainment=row['Guardian Educational Attainment'],
                    guardian_employer=row['Guardian Employer'],
                    guardian_occupation=row['Guardian Occupation'],
                )
                applicant.save()
                applicant_count += 1

            messages.success(request, f'{applicant_count} applicant(s) imported successfully.')
            return redirect('applicant_list')
    
    else:
        form = ApplicantUploadForm()
    return render(request, 'import.html', {'form': form})

#-----------------------------------------------------------------------------

 
#export ----------------------------------------------------------------------------------------------------------------------------------

def csv_record(request):
    if request.method == 'POST':
        form = ExportForm(request.POST)

        if form.is_valid():
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=record.csv'

            writer = csv.writer(response)

            include_id = form.cleaned_data.get('include_id', False)
            include_name = form.cleaned_data.get('include_name', False)
            include_course = form.cleaned_data.get('include_course', False)
            include_school = form.cleaned_data.get('include_school', False)

            headers = []
            if include_id:
                headers.append('ID')
            if include_name:
                headers.append('Name')
            if include_course:
                headers.append('Course')
            if include_school:
                headers.append('School')

            writer.writerow(headers)

            records = CollegeStudentApplication.objects.all()

            for record in records:
                row = []
                if include_id:
                    row.append(record.id)
                if include_name:
                    row.append(str(record))
                if include_course:
                    row.append(record.course)
                if include_school:
                    row.append(record.school)

                writer.writerow(row)

            return response
    else:
        form = ExportForm()

    return render(request, 'export_form.html', {'form': form})


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



def home(request):
        return render(request, 'home.html', {})

# Login  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login_user(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['user_password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Incorrect username or password.")
    return render(request, 'login.html')
  

def logout_user (request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return render(request, 'home.html', {})

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate (username=username, password=password)
            login(request, user)
            messages.success(request, "Account Successfully Registered")
            return redirect('home')
    else:
        form = SignUpForm()  
        return render(request, 'signup.html', {'form': form})
    
    return render(request, 'signup.html', {'form': form})
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#render data in dashboard
def data_visualization(request):
    school_counts = (
        CollegeStudentApplication.objects
        .values('school')
        .exclude(school='0')
        .annotate(count=Count('school'))
        .order_by('-count')
    )

    total_students = sum(school_count['count'] for school_count in school_counts)

    students_per_school = {}
    for school_count in school_counts:
        school = school_count['school']
        count = school_count['count']
        students_per_school[school] = count

    data = []
    labels = []
    for school_count in school_counts:
        percentage = (school_count['count'] / total_students) * 100
        labels.append(school_count['school'])
        data.append(percentage)

    if not request.session.get('login_message_displayed', False):
        messages.success(request, "You have logged in successfully!")
        request.session['login_message_displayed'] = True

    return render(request, 'dashboard.html', {'labels': labels, 'data': data, 'count': total_students, 'students_per_school': students_per_school})
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#CRUD
def view_applicant_table(request):
    StudentRecords = CollegeStudentApplication.objects.all()

    if not request.session.get('login_message_displayed', False):
        messages.success(request, "You have logged in successfully!")
        request.session['login_message_displayed'] = True

    return render(request, 'applicant_list.html', {'StudentRecords': StudentRecords})

def applicant_information(request, pk):
    if request.user.is_authenticated:
        StudentRecords = CollegeStudentApplication.objects.get(id = pk)
        return render (request, 'applicants_info.html',{'StudentRecords': StudentRecords})
    else:
        messages.success(request, "You need to be Logged in to see this Data!")
        return redirect('home')
    

def delete_information(request, pk):
    if request.user.is_authenticated:
        delete_record = CollegeStudentApplication.objects.get(id = pk)
        delete_record.delete()
        messages.success(request, "Record has been deleted")
        return redirect('applicant_list')
    else:
        messages.success(request, "You need to be Logged in for this process")
        return redirect('home')
    

def add_information(request):  
    form =  AddApplicantForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save() 
                messages.success(request, "Record Successfully Added")
                return redirect('applicant_list')  
        return render(request, 'add_record.html', {'form': form}) 
    else:
        messages.error(request, "You need to be logged in for this process.")
        return redirect('home')
    
    
def update_information(request, pk):
    if request.user.is_authenticated:
        current_record = CollegeStudentApplication.objects.get(id = pk)
        form =  AddApplicantForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!!")
            return redirect("applicant_list")
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.error(request, "You need to be logged in for this process.")
        return redirect('home')
  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
#Navbar
def navbar_user(request):
    active_user = {'user' : request.user}

    return render(request, 'navbar.html', active_user)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  
   
