# Generated by Django 3.2.6 on 2021-08-29 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0017_auto_20210829_1031"),
        ("department", "0003_auto_20210829_1101"),
    ]

    operations = [
        migrations.CreateModel(
            name="DepartmentHeadTeacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "department",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="head_teacher",
                        to="department.department",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="head_teacher",
                        to="staff.staff",
                    ),
                ),
            ],
        ),
    ]
