# Generated by Django 3.2.6 on 2021-09-07 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0032_alter_staffcontacts_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffexperience',
            name='overall',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='staffexperience',
            name='pedagogical',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
