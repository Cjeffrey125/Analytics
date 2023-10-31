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

    path('Delete_Record/<str:pk>/<str:model_name>/', views.delete_record, name='delete_record'),
    path('Add_IskolarngBayan_Applicant/', views.add_information, {'form_type': 'applicant'}, name='add_applicant'),
    path('Add_FinancialAssistance_Applicant/', views.add_information, {'form_type': 'financial_assistance'}, name='add_financial_assistance'),
    path('Update_Record/<int:pk>', views.update_information, name='update_record'),

#------------------------------------------------------------------------------------------------------------------------------
    path('Applicant_List/', views.view_applicant_table, name='inb_applicant_list'),
    path('INB_Applicant_Info/<int:pk>/', views.inb_applicant_information, name='inb_applicant_info'),
    path('inb_requirements_list/<str:control_number>', views.inb_requirements_list, name='inb_requirements_list'),
    path('inb_filter_applicants/', views.inb_filter_applicants, name='inb_filter_applicants'),
    path('passed_applicant/', views.passed_applicant, name='passed_applicant'),
    path('passed_applicant_info/<str:control_number>/', views.passed_applicant_info, name='passed_applicant_info'),
    path('failed_applicant/', views.rejected_applicant, name='failed_applicant'),
    path('failed_applicant_info/<str:control_number>/', views.failed_applicant_info, name='failed_applicant_info'),
#-------------------------------------------------------------------------------------------------------------------------------
    path('Financial_Assistance_List/', views.financial_assistance_list, name='fa_applicant_list'),
    path('FA_Applicant_Info/<int:pk>/', views.fa_applicant_information, name='fa_applicant_info'),
    path('fa_filter_applicants/', views.inb_filter_applicants, name='fa_filter_applicants'),

    path('FA_Requirements/<str:control_number>/', views.fa_requirement_list, name='fa_requirements_list'),



]

