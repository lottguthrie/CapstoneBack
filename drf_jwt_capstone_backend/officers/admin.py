from django.contrib import admin
from .models import DailyReport, Officers
# Register your models here.


admin.site.register(Officers)
admin.site.register(DailyReport)