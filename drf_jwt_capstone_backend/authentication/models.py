from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE



# Create your models here.

# To add new columns to the authentication_user table include the properties
# in the model below
# In order for the new columns to appear in the database run:
# 1. python manage.py makemigrations
# 2. python manage.py migrate


class User(AbstractUser):
    # Shared between officers and supervisors
    last_name = models.CharField(max_length=20)    
    


    # Admin specific fields
    last_name = models.CharField(max_length=50, unique = True, blank= True, null= True)

    # Officer fields
    officer_id = models.IntegerField(blank=True, null= True, default=0)




    
    
    
