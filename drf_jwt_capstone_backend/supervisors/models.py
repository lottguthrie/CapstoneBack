
from django.db import models

# Create your models here.

class Supervisors(models.Model):    
    supervisor_id = models.IntegerField(blank=True, null= True, default=0)
    officer_id = models.IntegerField(blank=True, null= True, default=0)
    last_name = models.CharField(max_length=20, blank=True, null= True)
    first_name = models.CharField(max_length=20, blank=True, null= True)
    middle_name = models.CharField(max_length=20, blank=True, null= True)
    badge_number = models.IntegerField(blank=True, null= True, default=0)
    is_active = models.BooleanField(blank=False, null=True)
    
    


class SupervisorReport(models.Model):
    supervisor_report_id = models.IntegerField(blank=True, null= True, default=0)
    supervisor_id = models.IntegerField(blank=True, null= True, default=0)
    date = models.DateTimeField(auto_now_add=False)
    total_calls_for_service = models.IntegerField(blank=True, null= True, default=0)
    total_case_numbers_pulled = models.IntegerField(blank=True, null= True, default=0)
    total_case_numbers_completed = models.IntegerField(blank=True, null= True, default=0)
    total_reports = models.IntegerField(blank=True, null= True, default=0)
    total_supplements = models.IntegerField(blank=True, null= True, default=0)
    total_vehicles_assigned = models.IntegerField(blank=True, null= True, default=0)
    total_miles_driven = models.IntegerField(blank=True, null= True, default=0)
    officers_on_road = models.IntegerField(blank=True, null= True, default=0)
    officers_on_desk = models.IntegerField(blank=True, null= True, default=0)
    officers_on_jail_duty = models.IntegerField(blank=True, null= True, default=0)
    officers_on_light_duty = models.IntegerField(blank=True, null= True, default=0)
    officers_out_sick = models.IntegerField(blank=True, null= True, default=0)
    officers_in_training = models.IntegerField(blank=True, null= True, default=0)
    officers_on_vacation = models.IntegerField(blank=True, null= True, default=0)
    officers_assigned_elswhere = models.IntegerField(blank=True, null= True, default=0)
    total_citations_issued = models.IntegerField(blank=True, null= True, default=0)
    total_warnings_issued = models.IntegerField(blank=True, null= True, default=0)
    total_citizen_contacts = models.IntegerField(blank=True, null= True, default=0)
    total_traffic_stops = models.IntegerField(blank=True, null= True, default=0)
    total_arrest_made = models.IntegerField(blank=True, null= True, default=0)
    total_juvenile_contacts = models.IntegerField(blank=True, null= True, default=0)


