# Generated by Django 3.2.6 on 2021-08-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0005_auto_20210829_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departmentcontacts',
            name='second_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]