# Generated by Django 3.2.6 on 2021-09-06 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0012_alter_departmentreward_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='pps_info',
        ),
        migrations.RemoveField(
            model_name='department',
            name='pps_info_en',
        ),
        migrations.RemoveField(
            model_name='department',
            name='pps_info_ky',
        ),
        migrations.RemoveField(
            model_name='department',
            name='pps_info_ru',
        ),
    ]
