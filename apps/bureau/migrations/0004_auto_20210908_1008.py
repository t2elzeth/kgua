# Generated by Django 3.2.6 on 2021-09-08 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0033_auto_20210907_1704'),
        ('bureau', '0003_auto_20210908_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bureaumember',
            name='bureau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='bureau.bureau'),
        ),
        migrations.AlterField(
            model_name='bureaumember',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bureau_members', to='staff.staff'),
        ),
    ]