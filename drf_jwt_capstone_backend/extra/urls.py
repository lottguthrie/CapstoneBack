from django.urls import path
from . import views


app_name = "extra"
urlpatterns = [    
    path('registerextra/', views.ExtraRegistration.as_view()),
    path('addextra/<str:name>', views.GetAllExtra.as_view()),
    path('extras/<str:officer_id>', views.ExtraData.as_view()),
    path('officerroleregistration/', views.OfficerRolesRegistration.as_view()),
    path('officerroles/', views.AllOfficerRoles.as_view()),
    path('officerroles/<int:pk>', views.OfficerRolesData.as_view())
]