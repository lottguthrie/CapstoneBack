# Generated by Django 3.2.8 on 2021-12-13 14:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supervisors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Officers',
            fields=[
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(blank=True, null= True, default=0)),
                ('email', models.EmailField(max_length=40, blank=True, null=True)),
                ('badge_number', models.IntegerField(blank=True, null= True, default=0)),
                ('officer_id', models.IntegerField(blank=True, null= True, default=0)),
                ('supervisor_id', models.IntegerField(blank=True, null= True, default=0)),
                ('is_active', models.BooleanField(blank=False, null=True)),
                ('is_supervisor', models.BooleanField(blank=False, null=True)) 
            ],
        ),
    
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('report_id', models.IntegerField(blank=True, null= True, default=0)),
                ('officer_id', models.IntegerField(blank=True, null= True, default=0)),
                ('date', models.DateField(auto_now_add=False)),
                ('calls_for_service', models.IntegerField(blank=True, null= True, default=0)),
                ('reports', models.IntegerField(blank=True, null= True, default=0)),
                ('supplements', models.IntegerField(blank=True, null= True, default=0)),
                ('citations_issued', models.IntegerField(blank=True, null= True, default=0)),
                ('warnings_issued', models.IntegerField(blank=True, null= True, default=0)),
                ('traffic_stops', models.IntegerField(blank=True, null= True, default=0)),
                ('citizen_contacts', models.IntegerField(blank=True, null= True, default=0)),
                ('juvenile_contacts', models.IntegerField(blank=True, null= True, default=0)),
                ('assigned_area', models.CharField(max_length=20, blank=True, null= True)),
                ('assigned_vehicle', models.IntegerField(blank=True, null= True, default=0)),
                ('miles_driven', models.IntegerField(blank=True, null= True, default=0)),
                ('hours_worked', models.IntegerField(blank=True, null= True, default=0)),
                ('case_numbers', models.CharField(max_length=20, blank=True, null= True))
            ],
        ),
    ]
