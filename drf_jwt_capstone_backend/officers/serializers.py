from rest_framework import serializers
from .models import DailyReport, Officers

class OfficersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officers
        fields = ['username', 'last_name', 'first_name', 'middle_name', 'phone_number', 'email', 'badge_number', 'officer_id', 'supervisor_id', 'is_active', 'is_supervisor']
        
    

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyReport
        fields = ['username', 'report_id', 'officer_id', 'date', 'calls_for_service', 'reports', 'supplements', 'citations_issued', 'warnings_issued', 'traffic_stops', 'citizen_contacts', 'juvenile_contacts', 'assigned_area', 'assigned_vehicle', 'miles_driven', 'hours_worked', 'case_numbers']
        
            