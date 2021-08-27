# Generated by Django 3.2.6 on 2021-08-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kgua_life", "0003_charity_promotion"),
    ]

    operations = [
        migrations.CreateModel(
            name="Club",
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
            ],
            options={
                "verbose_name": "Клуб",
                "verbose_name_plural": "Клубы",
            },
        ),
        migrations.CreateModel(
            name="Jubilee",
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
            ],
            options={
                "verbose_name": "Юбилей",
                "verbose_name_plural": "Юбилеи",
            },
        ),
        migrations.CreateModel(
            name="Mug",
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
            ],
            options={
                "verbose_name": "Кружок",
                "verbose_name_plural": "Кружки",
            },
        ),
    ]
