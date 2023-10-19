from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Login/', views.login_user, name='login'),
    path('Logout/', views.logout_user, name='logout'),
    path('SignUp/', views.register_user, name='signup'),
    path('Dashboard/', views.data_visualization, name='dashboard'),
    path('Applicant_List/', views.view_applicant_table, name='applicant_list'),
    path('Applicant_Info/<int:pk>', views.applicant_information, name='applicant_info'),
    path('Delete_Record/<int:pk>', views.delete_information, name='delete_record'),
    path('Add_Record', views.add_information, name='add_record'),
    path('Update_Record/<int:pk>', views.update_information, name='update_record'),

    path('CSV_Record', views.csv_record, name = 'export'),
    path('Import_File/', views.import_excel, name = 'import'),

    path('requirements/<str:control_number>', views.requirements_view, name='requirements'),

]
