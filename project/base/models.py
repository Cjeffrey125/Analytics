from django.db import models

class CollegeStudentApplication(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)

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
    
    def save(self, *args, **kwargs):
        created = not self.pk  
        super().save(*args, **kwargs) 

        if created:
            CollegeRequirements.objects.create(control=self)
            

class CollegeRequirements(models.Model):
    control = models.ForeignKey(CollegeStudentApplication, on_delete=models.CASCADE)
    control_number = models.CharField(max_length=50, default='')
    requirement = models.IntegerField(default=0)

    req_a = models.CharField(max_length=100, default='False')
    req_b = models.CharField(max_length=100, default='False')
    req_c = models.CharField(max_length=100, default='False')
    req_d = models.CharField(max_length=100, default='False')
    req_e = models.CharField(max_length=100, default='False')
    req_f = models.CharField(max_length=100, default='False')
    req_g = models.CharField(max_length=100, default='False')
    req_h = models.CharField(max_length=100, default='False')
    req_i = models.CharField(max_length=100, default='False')
    req_j = models.CharField(max_length=100, default='False')
    req_k = models.CharField(max_length=100, default='False')
    req_l = models.CharField(max_length=100, default='False')
    req_m = models.CharField(max_length=100, default='False')

    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Requirements for Application {self.control, self.control_number}"

    def save(self, *args, **kwargs):
        if not self.control_number:
            self.control_number = self.control.control_number

        requirement_fields = [self.req_a, self.req_b, self.req_c, self.req_d, self.req_e, self.req_f,
                             self.req_g, self.req_h, self.req_i, self.req_j, self.req_k, self.req_l, self.req_m]
        self.requirement = sum(1 for field in requirement_fields if field.strip() == 'True')

        super().save(*args, **kwargs)


class CollegeStudentAccepted(models.Model):
    control_number = models.CharField(primary_key=True, max_length=50)
    fullname = models.CharField(max_length=50)
    school_year = models.CharField(max_length=50, default='1st Years')
    course = models.CharField(max_length=50, default='')
    school = models.CharField(max_length=150, default='')

class CollegeStudentRejected(models.Model):
    control_number = models.CharField(primary_key=True, max_length=50)
    fullname = models.CharField(max_length=50)
    remarks = models.CharField(max_length=200, default="")
    


class ApplicantInfoRepositoryINB(models.Model): 

    control_number = models.CharField(unique=True, max_length=50)
    status = models.CharField(max_length=20, choices=(("Accepted", "Accepted"), ("Rejected", "Rejected"))) 
  

    fullname = models.CharField(max_length=250, default='')  
    
    address = models.CharField(max_length=100, default='Unknown')

    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(default='2001-01-01')
    place_of_birth = models.CharField(max_length=100, default='')
    contact_no = models.CharField(max_length=25, default='')

    email_address = models.EmailField(max_length=100, default='')
    school = models.CharField(max_length=150, default='')

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
        return self.fullname


#----------------------------------------------------------------------------------------------------------------------------
class FinancialAssistanceApplication(models.Model): 

    control_number = models.CharField(unique=True, max_length=50)

    #personal data
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, default='')  
    suffix = models.CharField(max_length=50, default='')  

    date_of_birth = models.DateField(default='01-01-2001')
    place_of_birth = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=50)
    religion = models.CharField(max_length=100, default='')

    address = models.CharField(max_length=100, default='Unknown')
    email_address = models.EmailField(max_length=100, default='')
    contact_no = models.CharField(max_length=25, default='')
    general_average = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) 
    
    school = models.CharField(max_length=100, default='')
    school_address = models.CharField(max_length=100, default='')

    track = models.CharField(max_length=100, default='')
    strand = models.CharField(max_length=100, default='')
    
    #family data
    father_name = models.CharField(max_length=100, default='')
    father_age = models.SmallIntegerField(default='')
    father_occupation = models.CharField(max_length=100, default='')
    father_employer = models.CharField(max_length=100, default='')
    father_income = models.IntegerField(default='')

    mother_name = models.CharField(max_length=100, default='')
    mother_age = models.SmallIntegerField(default='')
    mother_occupation = models.CharField(max_length=100, default='')
    mother_employer = models.CharField(max_length=100, default='')
    mother_income = models.IntegerField(default='')

    sibling_count = models.SmallIntegerField(default='')

    sibling_name = models.CharField(max_length=100, default='')
    sibling_DOB = models.DateField(default='01-01-2001')
    sibling_age = models.SmallIntegerField(default=0)
    sibling_address = models.CharField(max_length=100, default='')


    def __str__(self):
        return f"{self.last_name}, {self.first_name} {self.middle_name}"

    def save(self, *args, **kwargs):
        created = not self.pk  
        super().save(*args, **kwargs) 
        
        if created:
            FinancialAssistanceRequirement.objects.create(control=self)
    

class FinancialAssistanceRequirement(models.Model):
    control = models.ForeignKey(FinancialAssistanceApplication, on_delete=models.CASCADE)
    control_number = models.CharField(max_length=50, default='')
    requirement = models.IntegerField(default=0)

    req_a = models.CharField(max_length=100, default='False')
    req_b = models.CharField(max_length=100, default='False')
    req_c = models.CharField(max_length=100, default='False')
    req_d = models.CharField(max_length=100, default='False')
    req_e = models.CharField(max_length=100, default='False')
    req_f = models.CharField(max_length=100, default='False')
    req_g = models.CharField(max_length=100, default='False')
    req_h = models.CharField(max_length=100, default='False')


    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Requirements for Application {self.control, self.control_number}"

    def save(self, *args, **kwargs):
        if not self.control_number:
            self.control_number = self.control.control_number

        requirement_fields = [self.req_a, self.req_b, self.req_c, self.req_d, self.req_e, self.req_f,
                             self.req_g, self.req_h]
        self.requirement = sum(1 for field in requirement_fields if field.strip() == 'True')

        super().save(*args, **kwargs)

class FinancialAssistanceAccepted(models.Model):
    control_number = models.CharField(primary_key=True, max_length=50)
    fullname = models.CharField(max_length=50)
    school_year = models.CharField(max_length=50, default='1st Years')
    course = models.CharField(max_length=50, default='')
    school = models.CharField(max_length=50, default='')

class FinancialAssistanceRejected(models.Model):
    control_number = models.CharField(primary_key=True, max_length=50)
    fullname = models.CharField(max_length=50)
    remarks = models.CharField(max_length=200, default="")


class FinancialAssistanceInfoRepository(models.Model): 

    control_number = models.CharField(unique=True, max_length=50)
    status = models.CharField(max_length=20, choices=(("Accepted", "Accepted"), ("Rejected", "Rejected"))) 
  

    fullname = models.CharField(max_length=250, default='')  

    date_of_birth = models.DateField(default='01-01-2001')
    place_of_birth = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=50)
    religion = models.CharField(max_length=100, default='')

    address = models.CharField(max_length=100, default='Unknown')
    email_address = models.EmailField(max_length=100, default='')
    contact_no = models.CharField(max_length=25, default='')
    general_average = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) 
    
    school = models.CharField(max_length=100, default='')
    school_address = models.CharField(max_length=100, default='')

    track = models.CharField(max_length=100, default='')
    strand = models.CharField(max_length=100, default='')
    
    #family data
    father_name = models.CharField(max_length=100, default='')
    father_age = models.SmallIntegerField(default='')
    father_occupation = models.CharField(max_length=100, default='')
    father_employer = models.CharField(max_length=100, default='')
    father_income = models.IntegerField(default='')

    mother_name = models.CharField(max_length=100, default='')
    mother_age = models.SmallIntegerField(default='')
    mother_occupation = models.CharField(max_length=100, default='')
    mother_employer = models.CharField(max_length=100, default='')
    mother_income = models.IntegerField(default='')

    sibling_count = models.SmallIntegerField(default='')

    sibling_name = models.CharField(max_length=100, default='')
    sibling_DOB = models.DateField(default='01-01-2001')
    sibling_age = models.SmallIntegerField(default=0)
    sibling_address = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.fullname


    

   