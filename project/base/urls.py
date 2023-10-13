from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Login/', views.login_user, name='login'),
    path('Logout/', views.logout_user, name='logout'),
    path('SignUp/', views.register_user, name='signup'),
    path('Dashboard/', views.data_visualization, name='dashboard'),
    path('Applicant_List/', views.view_applicant_table, name='applicant_list'),
    path('Applicant_Info/<str:control_number>', views.applicant_information, name='student_info'),
    path('Delete_Record/<str:control_number>', views.delete_information, name='delete_record'),
    path('Add_Record', views.add_information, name='add_record'),
    path('Update_Record/<str:control_number>/', views.update_information, name='update_record'),

    path('CSV_Record', views.csv_record, name = 'export'),
    path('Import_File/', views.import_excel, name = 'import')

]
