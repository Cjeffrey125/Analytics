from import_export import resources, fields, widgets
from import_export.widgets import DateWidget
from django.utils.dateparse import parse_date
from .models import CollegeStudentApplication

class CollegeStudentApplicationResource(resources.ModelResource):
    control_number = fields.Field(column_name= 'Control Number', attribute = 'control_number')
    last_name = fields.Field(column_name= 'Surname', attribute = 'last_name')
    first_name = fields.Field(column_name= 'Firstname', attribute = 'first_name')
    middle_name = fields.Field(column_name= 'Middlename', attribute = 'middle_name')
    address = fields.Field(column_name= 'Address', attribute = 'address')
    gender = fields.Field(column_name= 'Gender', attribute = 'gender' )
    date_of_birth = fields.Field(column_name='Date of Birth', attribute='date_of_birth', widget=DateWidget(format='%Y-%m-%d'))
    place_of_birth = fields.Field(column_name= 'Place of Birth', attribute = 'place_of_birth')
    contact_no = fields.Field(column_name= 'Contact No.', attribute = 'contact_no')
    email_address = fields.Field(column_name= 'Email Address', attribute = 'email_address' )
    school = fields.Field(column_name= 'Preferred School', attribute = 'school')
    course = fields.Field(column_name= 'Desired Course', attribute = 'course')
    gwa = fields.Field(column_name= 'GWA', attribute = 'gwa')
    rank = fields.Field(column_name= 'Rank',  attribute = 'rank')
    jhs = fields.Field(column_name= 'JHS', attribute = 'jhs' )
    jhs_address = fields.Field(column_name= 'JHS Address', attribute = 'jhs_address')
    jhs_educational_provider = fields.Field(column_name= 'Education Provider', attribute = 'jhs_educational_provider' )
    shs = fields.Field(column_name= 'SHS', attribute = 'shs')
    shs_address = fields.Field(column_name= 'SHS Address', attribute = 'shs_address' )
    shs_educational_provider = fields.Field(column_name= 'Education Provider', attribute = 'shs_educational_provider' )

    father_name = fields.Field(column_name= 'Father Name', attribute = 'father_name' )
    father_voter_status = fields.Field(column_name= 'Father Voter Status', attribute = 'father_voter_status' )
    father_educational_attainment = fields.Field(column_name= 'Father Educational Attainment', attribute = 'father_educational_attainment')
    father_occupation = fields.Field(column_name='Father Occupation', attribute = 'father_occupation')
    father_employer = fields.Field(column_name= 'Father Employer', attribute ='father_employer')
    
    mother_name = fields.Field(column_name= 'Mother Name', attribute = 'mother_name')
    mother_voter_status = fields.Field(column_name= 'Mother Voter Status', attribute = 'mother_voter_status')
    mother_educational_attainment = fields.Field(column_name= 'Mother Educational Attainment', attribute = 'mother_educational_attainment')
    mother_occupation = fields.Field(column_name='Mother Occupation', attribute ='mother_occupation')
    mother_employer = fields.Field(column_name= 'Mother Employer', attribute = 'mother_employer')

    guardian_name = fields.Field(column_name= 'Legal Guardian', attribute = 'guardian_name')
    guardian_voter_status = fields.Field(column_name= 'Guardian Voter Status', attribute = 'guardian_voter_status')
    guardian_educational_attainment = fields.Field(column_name= 'Guardian Educational Attainment', attribute = 'guardian_educational_attainment')
    guardian_occupation = fields.Field(column_name='Guardian Occupation', attribute ='guardian_occupation')
    guardian_employer = fields.Field(column_name= 'Guardian Employer', attribute = 'guardian_employer')

    def dehydrate_date_of_birth(self, obj):
        try:
            return parse_date(obj.date_of_birth)
        except (ValueError, TypeError):
            return "Invalid Date"

    class Meta:
        model = CollegeStudentApplication
        import_id_fields = ('control_number',)
