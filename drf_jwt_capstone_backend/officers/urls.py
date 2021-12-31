from django.urls import path
from . import views


app_name = "officers"
urlpatterns = [    
    path('officers/<str:name>/', views.GetAllOfficers.as_view()),
    path('home/', views.AddOfficer.as_view()),
    path('officerdata/<int:pk>/', views.OfficerData.as_view()),
    path('addreport/', views.AddDailyReport.as_view()),
    path('dailyreport/<str:name>/', views.GetDailyReport.as_view()),
    path('editreport/', views.EditDailyReport.as_view()),
    
]