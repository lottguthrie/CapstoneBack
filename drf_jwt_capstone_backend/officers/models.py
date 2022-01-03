
from django.db import models
from django.db.models.deletion import CASCADE




# Create your models here.

class Officers(models.Model):    
    username = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    phone_number = models.IntegerField(blank=True, null= True, default=0)
    email = models.EmailField(max_length=40, blank=True, null=True)
    badge_number = models.IntegerField(blank=True, null= True, default=0)
    officer_id = models.IntegerField(blank=True, null= True, default=0)
    supervisor_id = models.IntegerField(blank=True, null= True, default=0)
    is_active = models.BooleanField(blank=False, null=True)
    is_supervisor = models.BooleanField(blank=False, null=True)

class DailyReport(models.Model):
    username = models.CharField(max_length=20)
    report_id = models.IntegerField(blank=True, null= True, default=0)
    officer_id = models.IntegerField(blank=True, null= True, default=0)
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
