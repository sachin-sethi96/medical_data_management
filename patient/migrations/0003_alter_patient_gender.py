# Generated by Django 4.2 on 2023-05-04 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6),
        ),
    ]
