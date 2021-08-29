# Generated by Django 3.2.6 on 2021-08-29 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("department", "0011_departmentreward_department"),
    ]

    operations = [
        migrations.AlterField(
            model_name="departmentreward",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rewards",
                to="department.department",
            ),
        ),
    ]
