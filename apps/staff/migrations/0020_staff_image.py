# Generated by Django 3.2.6 on 2021-08-29 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0019_staffreward'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]