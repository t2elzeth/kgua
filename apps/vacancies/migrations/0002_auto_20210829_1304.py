# Generated by Django 3.2.6 on 2021-08-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vacancies", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vacancykg",
            name="parent",
        ),
        migrations.RemoveField(
            model_name="vacancyru",
            name="parent",
        ),
        migrations.AddField(
            model_name="vacancy",
            name="description",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vacancy",
            name="description_en",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="vacancy",
            name="description_ky",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="vacancy",
            name="description_ru",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="vacancy",
            name="salary",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vacancy",
            name="title",
            field=models.CharField(default=1, max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="vacancy",
            name="title_en",
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name="vacancy",
            name="title_ky",
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name="vacancy",
            name="title_ru",
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.DeleteModel(
            name="VacancyEN",
        ),
        migrations.DeleteModel(
            name="VacancyKG",
        ),
        migrations.DeleteModel(
            name="VacancyRU",
        ),
    ]