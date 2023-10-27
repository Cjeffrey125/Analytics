from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from base.models import CollegeStudentApplication, FinancialAssistanceApplication

class ApplicantUploadForm(forms.Form):
    file = forms.FileField()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label = "", widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label = "", max_length = "50", widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label = "", max_length = "50", widget = forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ExportForm(forms.Form):
    include_id = forms.BooleanField(required=True, initial=True, label="Include Student ID")
    include_name = forms.BooleanField(required=False, initial=True, label="Include Student Name")
    include_school = forms.BooleanField(required=False, initial=True, label="Include Student School")
    include_course = forms.BooleanField(required=False, initial=True, label="Include Student Course")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class AddApplicantForm(forms.ModelForm):
        GENDER_CHOICES = [
            ("0", "Select Gender"),
            ("Male", "Male"),
            ("Female", "Female"),
        ]
        
        EDUCATIONAL_PROVIDERS = [
            ("0", "Choose Educational Provider"),
            ("Deped", "DepEd"),
            ("Non-Deped", "Non-DepEd"),
        ]

        SCHOOL_CHOICES = [
            ("0", "Preferred School"),
            ("Colegio San Agustin", "Colegio San Agustin"),
            ("Citi Global College", "Citi Global College"),
            ("Guardians Bonafide For Hope Foundation Philippines", "Guardians Bonafide For Hope Foundation Philippines"),
            ("La Consolacion College", "La Consolacion College"),
            ("Polytechnic University of the Philippines - Biñan Campus", "Polytechnic University of the Philippines - Biñan Campus"),
            ("Trimex Colleges", "Trimex Colleges"),
            ("Saint Michaels College of Laguna", "Saint Michaels College of Laguna"),
            ("UPH-DR. Jose G. Tamayo Medical University", "UPH-DR. Jose G. Tamayo Medical University"),
            ("University of Perpetual Help System Laguna", "University of Perpetual Help System Laguna")
        ]

        COURSES_OFFERED = [
            ("0", "Choose Course"),
            ("BS Psychology", "BS Psychology"),
            ("BS Foreign Service", "BS Foreign Service"),
            ("BS Computer Science", "BS Computer Science"),
            ("BS Information Technology", "BS Information Technology"),
            ("Bachelor of Technical-Vocational Teacher Education", "Bachelor of Technical-Vocational Teacher Education"),
            ("BS Criminology", "BS Criminology"),
            ("BS Accountancy", "BS Accountancy"),
            ("Bachelor of Elementary Education", "Bachelor of Elementary Education"),
            ("BSED English", "BSED English"),
            ("BSED Filipino", "BSED Filipino"),
            ("BSED Social Studies", "BSED Social Studies"),
            ("BS Computer Engineering", "BS Computer Engineering"),
            ("BS Industrial Engineering", "BS Industrial Engineering"),
            ("BS Social Work", "BS Social Work"),
            ("BS Nursing", "BS Nursing"),
            ("BSED Math", "BSED Math"),
            ("Doctor of Dental Medicine", "Doctor of Dental Medicine"),
            ("Medical Technology", "Medical Technology"),
            ("Midwifery", "Midwifery"),
            ("Nursing", "Nursing"),
            ("Occupational Therapy", "Occupational Therapy"),
            ("Pharmacy", "Pharmacy"),
            ("Physical Therapy", "Physical Therapy"),
            ("Pharmacy", "Pharmacy"),
            ("Radiologic Technology", "Radiologic Technology"),
            ("BS Architecture", "BS Architecture"), 
            ("Bachelor of Library and Information Science", "Bachelor of Library and Information Science"),
            ("Bachelor of Early Childhood Education", "Bachelor of Early Childhood Education"),
            ("Bachelor of Physical Education", "Bachelor of Physical Education"),
            ("Bachelor of Special Needs Education - Generalist", "Bachelor of Special Needs Education - Generalist"),
            ("Bachelor of Technology & Livelihood Education", "Bachelor of Technology & Livelihood Education"),
            ("Bachelor of Secondary Education", "Bachelor of Secondary Education"),
            ("BS Civil Engineering", "BS Civil Engineering"),
            ("BS Electrical Engineering", "BS Electrical Engineering"),
            ("BS Electronics Engineering", "BS Electronics Engineering"), 
            ("BS Mechanical Engineering", "BS Mechanical Engineering"),
            ("BS Nutrition and Dietetics", "BS Nutrition and Dietetics"),
        ]

        VOTER_STATUS = [
            ("0", "Select Status"),
            ("Registered Voter", "Registered Voter"),
            ("Not Registered Voter", "Not Registered Voter"),
        ]
        

        control_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Control Number", "class":"form-control"}), label="")
        
        #Personal Data
        first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">First Name</span>', label="")
        last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}),  help_text='<span class="subscript">Surname</span>', label="")
        middle_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">Middle Name</span>', label="")

        address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">Address</span>', label="")

        gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES, widget=forms.Select(attrs={"class": "form-control"}), label="")

        date_of_birth = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget(attrs={"class": "form-control"}),
        help_text='<span class="subscript">Date of Birth</span>',
        label="Date of Birth")

        place_of_birth = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Place of Birth", "class":"form-control"}), label="")
        contact_no = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contact No", "class":"form-control"}), label="")

        email_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email Address","class":"form-control"}), label="")
        school = forms.ChoiceField(required=True, choices=SCHOOL_CHOICES, widget=forms.Select(attrs={"class": "form-control"}), label="")

        course = forms.ChoiceField(required=True, choices=COURSES_OFFERED, widget=forms.Select(attrs={"class": "form-control"}), label="")
        gwa =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"General Weighted Average", "class":"form-control"}), label="")
        rank = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Rank", "class":"form-control"}), label="")

        jhs = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Junior High School", "class":"form-control"}), label="")
        jhs_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"SHS Address", "class":"form-control"}), label="")
        jhs_educational_provider = forms.ChoiceField(required=True, choices=EDUCATIONAL_PROVIDERS, widget=forms.Select(attrs={"class": "form-control"}), label="")
        
        shs = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Senior High School", "class":"form-control"}), label="")
        shs_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"SHS Address", "class":"form-control"}), label="")
        shs_educational_provider = forms.ChoiceField(required=True, choices=EDUCATIONAL_PROVIDERS, widget=forms.Select(attrs={"class": "form-control"}), label="")

        #Family Data
        father_voter_status =  forms.ChoiceField(required=True, choices=VOTER_STATUS, widget=forms.Select(attrs={"class": "form-control"}), label="")
        father_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Father Name", "class":"form-control"}), label="")
        father_educational_attainment =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Educational Attainment", "class":"form-control"}), label="")
        father_occupation = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Occupation", "class":"form-control"}), label="")
        father_employer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Employer", "class":"form-control"}), label="")

        mother_voter_status =  forms.ChoiceField(required=True, choices=VOTER_STATUS, widget=forms.Select(attrs={"class": "form-control"}), label="")
        mother_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mother Name", "class":"form-control"}), label="")
        mother_educational_attainment = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Educational Attainment", "class":"form-control"}), label="")
        mother_occupation = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Occupation", "class":"form-control"}), label="")
        mother_employer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Employer", "class":"form-control"}), label="")

        guardian_voter_status =  forms.ChoiceField(required=True, choices=VOTER_STATUS, widget=forms.Select(attrs={"class": "form-control"}), label="")
        guardian_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Legal Guardian Name", "class":"form-control"}), label="")
        guardian_educational_attainment = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Educational Attainment", "class":"form-control"}), label="")
        guardian_occupation = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Occupation", "class":"form-control"}), label="")
        guardian_employer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Employer", "class":"form-control"}), label="")

        class Meta:
            model = CollegeStudentApplication
            
            exclude = ("user",)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class AddFinancialAssistanceForm(forms.ModelForm):
    GENDER_CHOICES = [
        ("0", "Select Gender"),
        ("Male", "Male"),
        ("Female", "Female"),
    ]
     
    SCHOOL_CHOICES = [
        ("0", "Preferred School"),
        ("Biñan Secondary School of Applied Academics", "Biñan Secondary School of Applied Academics"),
        ("Biñan Integrated National High School", "Biñan Integrated National High School"),
        ("Saint Francis National High School", "Saint Francis National High School"),
        ("Southville 5-A National High School",  "Southville 5-A National High School"),
        ("Jacobo Z. Gonzales Memorial National High School",  "Jacobo Z. Gonzales Memorial National High School"),
        ("Dela Paz National High School", "Dela Paz National High School"),
        ("Biñan City Science and Technology High School", "Biñan City Science and Technology High School"),
        ("Mamplasan National High School", "Mamplasan National High School"),
        ("Nereo R. Joaquin National High School", "Nereo R. Joaquin National High School"),
    ]

    STRAND_CHOICE = [
        ("0", "Preferred Strand"),
        ('ABM', 'Accountancy, Business, and Management'),
        ('HUMSS', 'Humanities and Social Sciences'),
        ('STEM', 'Science, Technology, Engineering, and Mathematics'),
        ('GAS', 'General Academic Strand'),
        ('TVL', 'Technical Vocational Livelihood (TVL) Track'),
        ('Sports', 'Sports Track'),
        ('ArtsAndDesign', 'Arts and Design Track'),
    ]

    TRACK_CHOICE = [
        ("0", "Preferred Track"),
        ('Academic Track', 'Academic Track'),
        ('Vocational Track', 'Vocational Track'),
        ('Technical Track', 'Technical Track'),
    ]
    
    control_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Control Number", "class":"form-control"}), label="")
        
    #Personal Data
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">First Name</span>', label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}),  help_text='<span class="subscript">Surname</span>', label="")
    middle_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">Middle Name</span>', label="")
    suffix = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">Suffix</span>', label="")

    date_of_birth = forms.DateField(
    required=True,
    widget=forms.SelectDateWidget(attrs={"class": "form-control"}),
    help_text='<span class="subscript">Date of Birth</span>',
    label="Date of Birth")

    place_of_birth = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Place of Birth", "class":"form-control"}), label="")
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES, widget=forms.Select(attrs={"class": "form-control"}), label="")
    religion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Religion", "class":"form-control"}), label="")

    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">Address</span>', label="")
    email_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email Address","class":"form-control"}), label="")
    
    contact_no = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Contact No", "class":"form-control"}), label="")
    general_average =  forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"General Weighted Average", "class":"form-control"}), label="")
    
    school = forms.ChoiceField(required=True, choices=SCHOOL_CHOICES, widget=forms.Select(attrs={"class": "form-control"}), label="")
    school_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"SHS Address", "class":"form-control"}), label="")
    track = forms.ChoiceField(required=True, choices=TRACK_CHOICE, widget=forms.Select(attrs={"class": "form-control"}), label="")
    strand = forms.ChoiceField(required=True, choices=STRAND_CHOICE, widget=forms.Select(attrs={"class": "form-control"}), label="")
    

    #Family Data
    father_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Father Name", "class":"form-control"}), label="")
    father_age = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Age", "class":"form-control"}), label="")
    father_income = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Income", "class":"form-control"}), label="")
    father_occupation = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Occupation", "class":"form-control"}), label="")
    father_employer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Employer", "class":"form-control"}), label="")

    mother_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Mother Name", "class":"form-control"}), label="")
    mother_age = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Age", "class":"form-control"}), label="")
    mother_income = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Income", "class":"form-control"}), label="")
    mother_occupation = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Occupation", "class":"form-control"}), label="")
    mother_employer = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Name of Employer", "class":"form-control"}), label="")

    sibling_count = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"No. of Siblings", "class":"form-control"}), label="")

    sibling_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">Name</span>', label="")
    sibling_DOB =  forms.DateField(
    required=True,
    widget=forms.SelectDateWidget(attrs={"class": "form-control"}),
    help_text='<span class="subscript">Date of Birth</span>',
    label="Date of Birth") 
    sibling_age = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Age", "class":"form-control"}), label="")
    sibling_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"class":"form-control"}), help_text='<span class="subscript">Address</span>', label="")

    class Meta:
        model = FinancialAssistanceApplication
        
        exclude = ("user",)