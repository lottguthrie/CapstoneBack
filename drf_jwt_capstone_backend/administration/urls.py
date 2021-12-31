from django.urls import path
from . import views



urlpatterns = [    
    path('registeradmin/', views.AdminRegistration.as_view()),
    path('addadmin/<str:name>', views.GetAllAdmin.as_view()),
    path('admins/<str:officer_id>', views.AdminData.as_view()),
    path('officerroleregistration/', views.OfficerRolesRegistration.as_view()),
    path('officerroles/', views.AllOfficerRoles.as_view()),
    path('officerroles/<int:pk>', views.OfficerRolesData.as_view())
]