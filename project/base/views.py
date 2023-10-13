from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from project.forms import SignUpForm, AddApplicantForm, ExportForm, ExcelImportForm
from .models import CollegeStudentApplication
from django.db.models import Count
from django.http import HttpResponse
import csv

from import_export.formats import base_formats
from import_export.resources import ModelResource
from tablib import Dataset

class CollegeStudentApplicationResource(ModelResource):
    class Meta:
        model = CollegeStudentApplication

#import ----------------------------------------------------------------------------------------------------------------------------------
def import_excel(request):
    if request.method == 'POST':
        form = ExcelImportForm(request.POST, request.FILES)  # Get the form data

        if form.is_valid():
            excel_file = request.FILES['excel_file']
            data = Dataset()

            data.load(excel_file.read(), format='xlsx')

  
            resource = CollegeStudentApplicationResource()
            result = resource.import_data(data, dry_run=False)

            if result.has_errors():
   
                pass
            else:
            
                return render(request, 'import_success.html')
    
    else:
        form = ExcelImportForm()
        
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
  
   
