# Generated by Django 3.2.6 on 2021-08-27 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0002_alter_staff_options"),
    ]

    operations = [
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
                ("from_year", models.IntegerField()),
                ("to_year", models.IntegerField()),
                ("description", models.TextField()),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="education",
                        to="staff.staff",
                    ),
                ),
            ],
        ),
    ]