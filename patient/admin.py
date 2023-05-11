from django.contrib import admin
from .models import Patient, Medication

# Register your models here.

class PatientAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Patient._meta.get_fields() if field.name != "medication"]
    ordering = ("registration_number",)


class MedicationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Medication._meta.get_fields()]
    list_display_links = ("patient", )


admin.site.register(Patient, PatientAdmin)
admin.site.register(Medication, MedicationAdmin)