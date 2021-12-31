from rest_framework import serializers
from .models import Admin, OfficerRoles


#class OwnersSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Owners
#        fields = ['business_name', 'username', 'first_name', 'last_name']
#
#class OwnersLoginSerializer(serializers.Serializer):
#    class Meta:
#        models = Owners
#        fields = ['business_name', 'username', 'first_name', 'last_name']

        

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ['training', 'evaluations', 'service_time', 'awards', 'officer_id']

class OfficerRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficerRoles
        fields = ['is_supervisor']