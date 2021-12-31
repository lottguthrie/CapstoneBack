from django.urls import path
from . import views


app_name = "supervisors"
urlpatterns = [    
    path('supervisor/<str:name>/', views.GetAllSupervisors.as_view()),
    path('supervisorhome/', views.AddSupervisor.as_view()),
    path('supervisordata/<int:pk>/', views.SupervisorData.as_view()),
    path('addsupervisorreport/', views.AddSupervisorReport.as_view()),
    path('supervisorreport/<str:name>/', views.GetSupervisorReport.as_view()),
    path('editsupervisorreport/', views.EditSupervisorReport.as_view()),    
    
]