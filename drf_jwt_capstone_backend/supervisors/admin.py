from django.contrib import admin
from .models import SupervisorReport, Supervisors
# Register your models here.


admin.site.register(Supervisors)
admin.site.register(SupervisorReport)


