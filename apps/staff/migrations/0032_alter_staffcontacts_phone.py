# Generated by Django 3.2.6 on 2021-09-06 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0031_auto_20210906_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffcontacts',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]