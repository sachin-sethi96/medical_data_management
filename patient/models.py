from django.db import models

# Create your models here.


class Patient(models.Model):

    gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
    ]

    location_choices = [
        ('D', 'Delhi'),
        ('N', 'NCR'),
        ('O', 'Outside Delhi')
    ]

    registration_number = models.AutoField(primary_key=True)
    time_stamp = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    name = models.CharField(max_length=100, unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=6, choices=gender_choices)
    contact_number = models.CharField(max_length=10)
    is_whatsapp_num = models.BooleanField()
    location = models.CharField(max_length=1, choices=location_choices)
    registered_by = models.CharField(max_length=31)



