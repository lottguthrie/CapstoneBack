from enum import unique
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

from drf_jwt_capstone_backend.administration.models import Admin
from drf_jwt_capstone_backend.supervisors.models import Supervisors

User = get_user_model()

# Create your models here.

class Officers(models.Model):    
    username=models.ForeignKey(User, to_field="username", on_delete = models.CASCADE)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(blank=True, null= True, default=0)
    email = models.EmailField(max_length=40, blank=True, null=True)
    badge_number = models.IntegerField(blank=True, null= True, default=0)
    officer_id = models.IntegerField(blank=True, null= True, default=0)
    supervisor_id = models.ForeignKey(Supervisors, to_field="supervisor_id", on_delete=CASCADE)
    is_active = models.BooleanField(blank=False, null=True)
    is_supervisor = models.ForeignKey(Admin, to_field="is_supervisor", on_delete=CASCADE)

class DailyReport(models.Model):
    username = models.ForeignKey(User, to_field="username", on_delete=CASCADE)
    report_id = ForeignKey(User, to_field="report_id", on_delete = models.CASCADE)
    officer_id = models.ForeignKey(Officers, to_field="officer_id", on_delete=CASCADE, blank = True, null = True)
    date = models.DateField(auto_now_add=False)
    calls_for_service = models.IntegerField(blank=True, null= True, default=0)
    reports = models.IntegerField(blank=True, null= True, default=0)
    supplements = models.IntegerField(blank=True, null= True, default=0)
    citations_issued = models.IntegerField(blank=True, null= True, default=0)
    warnings_issued = models.IntegerField(blank=True, null= True, default=0)
    traffic_stops = models.IntegerField(blank=True, null= True, default=0)
    citizen_contacts = models.IntegerField(blank=True, null= True, default=0)
    juvenile_contacts = models.IntegerField(blank=True, null= True, default=0)
    assigned_area = models.CharField(max_length=20, blank=True, null= True)
    assigned_vehicle = models.IntegerField(blank=True, null= True, default=0)
    miles_driven = models.IntegerField(blank=True, null= True, default=0)
    hours_worked = models.IntegerField(blank=True, null= True, default=0)
    case_numbers = models.CharField(max_length=20, blank=True, null= True)
