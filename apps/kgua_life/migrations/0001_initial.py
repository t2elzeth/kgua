# Generated by Django 3.2.4 on 2021-06-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("date", models.DateTimeField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=False)),
            ],
        ),
    ]