# Generated by Django 4.2 on 2023-05-06 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0007_medication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='registration_number',
            new_name='patient_id',
        ),
    ]
