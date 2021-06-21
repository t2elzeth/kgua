# Generated by Django 3.2.4 on 2021-06-21 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
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
                ("full_name", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("experience", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="StaffTraining",
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
                ("content", models.TextField()),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trainings",
                        to="staff.staff",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StaffEducation",
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
                ("content", models.TextField()),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="educations",
                        to="staff.staff",
                    ),
                ),
            ],
        ),
    ]
