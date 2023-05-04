from django.contrib import admin
from .models import Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Patient._meta.get_fields()]

admin.site.register(Patient, PatientAdmin)