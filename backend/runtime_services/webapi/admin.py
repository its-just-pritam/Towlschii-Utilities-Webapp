from django.contrib import admin
from .models import Company, ApplicationStatus, JobApplication

admin.site.register(Company)
admin.site.register(ApplicationStatus)
admin.site.register(JobApplication)

# Register your models here.
