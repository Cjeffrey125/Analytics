from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Login/', views.login_user, name='login'),
    path('Logout/', views.logout_user, name='logout'),
    path('SignUp/', views.register_user, name='signup'),
    path('Dashboard/', views.data_visualization, name='dashboard'),
    
    path('CSV_Record', views.csv_record, name = 'export'),
    path('Import_File/', views.import_excel, name = 'import'),

    path('delete_applicant/<str:model_name>/<str:pk>/', views.delete_record, name='delete_applicant'),


    path('Add_IskolarngBayan_Applicant/', views.add_information, {'form_type': 'applicant'}, name='add_inb_applicant'),
    path('Add_FinancialAssistance_Applicant/', views.add_information, {'form_type': 'financial_assistance'}, name='add_fa_applicant'),
    path('Update_Record/<int:pk>', views.update_information, name='update_inb_record'),
    path('Update_Record/<int:pk>', views.update_information, name='update_fa_record'),
   

#------------------------------------------------------------------------------------------------------------------------------
    path('Applicant_List/', views.view_applicant_table, name='inb_applicant_list'),
    path('INB_Applicant_Info/<int:pk>/', views.inb_applicant_information, name='inb_applicant_info'),
    path('inb_requirements_list/<str:control_number>', views.inb_requirements_list, name='inb_requirements_list'),
    path('inb_filter_applicants/', views.inb_filter_applicants, name='inb_filter_applicants'),

    path('inb/passed/applicant/', views.inb_applicant_list, {'status': 'passed'}, name='inb_passed_applicant'),
    path('inb/passed/applicant_info/<str:control_number>/', views.inb_applicant_info, {'status': 'passed'}, name='inb_passed_applicant_info'),
    path('inb/failed/applicant/', views.inb_applicant_list, {'status': 'failed'}, name='inb_failed_applicant'),
    path('inb/failed/applicant_info/<str:control_number>/', views.inb_applicant_info, {'status': 'failed'}, name='inb_failed_applicant_info'),


#-------------------------------------------------------------------------------------------------------------------------------
    path('Financial_Assistance_List/', views.financial_assistance_list, name='fa_applicant_list'),
    path('FA_Applicant_Info/<int:pk>/', views.fa_applicant_information, name='fa_applicant_info'),
    path('fa_filter_applicants/', views.fa_filter_applicants, name='fa_filter_applicants'),
    path('FA_Requirements/<str:control_number>/', views.fa_requirement_list, name='fa_requirements_list'),

    path('fa/<str:status>/applicant_info/<str:control_number>/', views.fa_applicant_info, name='fa_applicant_info'),

    path('fa/passed/applicant/', views.fa_applicant_list, {'status': 'passed'}, name='fa_passed_applicant'),
    path('fa/passed/applicant_info/<str:control_number>/', views.fa_applicant_info, {'status': 'passed'}, name='fa_passed_applicant_info'),
    path('fa/failed/applicant/', views.fa_applicant_list, {'status': 'failed'}, name='fa_failed_applicant'),
    path('fa/failed/applicant_info/<str:control_number>/', views.fa_applicant_info, {'status': 'failed'}, name='fa_failed_applicant_info'),
  




]

