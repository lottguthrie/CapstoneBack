from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

from drf_jwt_capstone_backend.officers.models import Officers



# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class Officer(AbstractUser):
    # Shared between officers and supervisors
    last_name = models.CharField(max_length=20)    
    


    # Admin specific fields
    last_name = models.CharField(max_length=50, unique = True, blank= True, null= True)

    # Officer fields
    officer_id = models.ForeignKey(Officers, to_field='last_name', null=True, on_delete=models.CASCADE)
    




    
    
    
