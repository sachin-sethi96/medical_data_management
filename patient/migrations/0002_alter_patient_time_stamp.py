# Generated by Django 4.2 on 2023-05-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='time_stamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]