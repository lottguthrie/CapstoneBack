
from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.

class Extra(models.Model):
    
    training: models.CharField(max_length=500)
    evaluations: models.FileField(("evaluations"), upload_to='uploads/ThisPC/Documents/', max_length=100)
    service_time: models.IntegerField(blank=True, null= True, default=0)
    awards: models.CharField(max_length=500)
    officer_id= models.IntegerField(blank=True, null= True, default=0)

class OfficerRoles(models.Model):
    is_supervisor: models.BooleanField(blank=False, null=True)