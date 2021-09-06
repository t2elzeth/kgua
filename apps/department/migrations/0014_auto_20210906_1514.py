# Generated by Django 3.2.6 on 2021-09-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0013_auto_20210906_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentreward',
            name='year',
        ),
        migrations.AddField(
            model_name='departmentreward',
            name='date',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='Дата получения'),
        ),
        migrations.AlterField(
            model_name='departmentcontacts',
            name='first_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='departmentcontacts',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
