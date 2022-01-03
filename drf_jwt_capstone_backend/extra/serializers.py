from rest_framework import serializers
from .models import Extra, OfficerRoles
        

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['training', 'evaluations', 'service_time', 'awards', 'officer_id']

class OfficerRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficerRoles
        fields = ['is_supervisor']