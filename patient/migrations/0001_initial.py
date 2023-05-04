# Generated by Django 4.2 on 2023-05-04 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('registration_number', models.AutoField(primary_key=True, serialize=False)),
                ('time_stamp', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('contact_number', models.CharField(max_length=10)),
                ('is_whatsapp_num', models.BooleanField()),
                ('location', models.CharField(choices=[('D', 'Delhi'), ('N', 'NCR'), ('O', 'Outside Delhi')], max_length=1)),
                ('registered_by', models.CharField(max_length=31)),
            ],
        ),
    ]
