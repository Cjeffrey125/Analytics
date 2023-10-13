from django.db import models

class CollegeStudentApplication(models.Model): 

    control_number = models.CharField(unique=True, max_length=50)

    #personal data
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default='')  

    address = models.CharField(max_length=100, default='Unknown')

    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(default='01-01-2001')
    place_of_birth = models.CharField(max_length=100, default='')
    contact_no = models.CharField(max_length=25, default='')

    email_address = models.EmailField(max_length=100, default='')
    school = models.CharField(max_length=100, default='')

    course = models.CharField(max_length=100, default='')
    gwa = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  
    rank = models.IntegerField(default=0)  

    jhs = models.CharField(max_length=100, default='')
    jhs_address = models.CharField(max_length=100, default='')
    jhs_educational_provider = models.CharField(max_length=100, default='')

    shs = models.CharField(max_length=100, default='')
    shs_address = models.CharField(max_length=100, default='')
    shs_educational_provider = models.CharField(max_length=100, default='')
    
    #family data
    father_voter_status = models.CharField(max_length=100, default='')
    father_name = models.CharField(max_length=100, default='')
    father_educational_attainment = models.CharField(max_length=100, default='')
    father_occupation = models.CharField(max_length=100, default='')
    father_employer = models.CharField(max_length=100, default='')

    mother_voter_status = models.CharField(max_length=100, default='')
    mother_name = models.CharField(max_length=100, default='')
    mother_educational_attainment = models.CharField(max_length=100, default='')
    mother_occupation = models.CharField(max_length=100, default='')
    mother_employer = models.CharField(max_length=100, default='')

    guardian_voter_status = models.CharField(max_length=100, default='')
    guardian_name = models.CharField(max_length=100, default='')
    guardian_educational_attainment = models.CharField(max_length=100, default='')
    guardian_occupation = models.CharField(max_length=100, default='')
    guardian_employer = models.CharField(max_length=100, default='')


    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"
    

class CollegeStudentAccepted(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    control_number = models.IntegerField(default=0) 
    fullname = models.CharField(max_length=50)
    school_year = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    grants = models.CharField(max_length=10, default='')
    semester = models.CharField(max_length=10, default='')
    remarks = models.CharField(max_length=50, default='')
    # grades??????

class CollegeStudentRejected(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    control_number =  models.IntegerField(default=0) 
    fullname = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    school_year = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)

