# Generated by Django 3.2.6 on 2021-08-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0015_auto_20210828_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='role',
            field=models.CharField(choices=[('teacher', 'teacher'), ('rector', 'rector')], max_length=512),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role_en',
            field=models.CharField(choices=[('teacher', 'teacher'), ('rector', 'rector')], max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role_ky',
            field=models.CharField(choices=[('teacher', 'teacher'), ('rector', 'rector')], max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='role_ru',
            field=models.CharField(choices=[('teacher', 'teacher'), ('rector', 'rector')], max_length=512, null=True),
        ),
    ]