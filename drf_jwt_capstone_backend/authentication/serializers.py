from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# from django.contrib.auth.models import Group
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
#from employees.models import Employees
#from owners.models import Owners
User = get_user_model()
#employees = Employees
#owners= Owners

class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        # Using existing flag is_staff as "is_owner" to leverage administrative privileges
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'middle_name', 'is_active') 

    def create(self, validated_data):
        
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            is_active=validated_data['is_active']            
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data['password'])
        user.save()

            

        return user

# Serializer for registering Users
class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'middle_name', 'is_active','officer_id') 

    def create(self, validated_data):
        #is_owner = validated_data["is_owner"]
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            middle_name=validated_data['middle_name'],
            is_active=validated_data['is_active'],
            officer_id=validated_data['officer_id']                                             
            # If added new columns through the User model, add them in this
            # create method call in the format as seen above
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'business_name', 'middle_name', 'is_active', 'officer_id')



