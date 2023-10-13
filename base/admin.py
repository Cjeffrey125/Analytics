from django.contrib import admin
from .models import CollegeStudentApplication, CollegeStudentAccepted ,CollegeStudentRejected
from import_export.admin import ImportExportModelAdmin
from .resources import CollegeStudentApplicationResource

class ImportFile(ImportExportModelAdmin):
    resource_class = CollegeStudentApplicationResource
    list_display = ('control_number', 'last_name', 'first_name', 'middle_name', 'address', 'gender', 'date_of_birth', 'place_of_birth', 'contact_no', 'email_address', 'school', 'course', 'gwa', 'rank', 'jhs', 'jhs_address', 'jhs_educational_provider', 'shs', 'shs_address', 'shs_educational_provider', 'father_name', 'father_voter_status', 'father_educational_attainment', 'father_employer', 'mother_name', 'mother_voter_status', 'mother_educational_attainment', 'mother_employer', 'guardian_name', 'guardian_voter_status', 'guardian_employer')

admin.site.register(CollegeStudentApplication, ImportFile)
admin.site.register(CollegeStudentAccepted)
admin.site.register(CollegeStudentRejected)