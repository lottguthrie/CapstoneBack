from enum import unique
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

from drf_jwt_capstone_backend.authentication.models import Officer
User = get_user_model()


# Create your models here.

class Admin(models.Model):
    
    training: models.CharField(max_length=500)
    evaluations: models.FileField(("evaluations"), upload_to='uploads/ThisPC/Documents/', max_length=100)
    service_time: models.IntegerField(blank=True, null= True, default=0)
    awards: models.CharField(max_length=500)
    officer_id= models.ForeignKey(Officer, to_field='officer_id', on_delete=models.CASCADE)

class OfficerRoles(models.Model):
    is_supervisor: models.BooleanField(blank=False, null=True)