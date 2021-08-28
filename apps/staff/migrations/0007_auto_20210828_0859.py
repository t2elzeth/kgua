# Generated by Django 3.2.6 on 2021-08-28 08:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0006_auto_20210828_0850"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stafftrainingkg",
            name="parent",
        ),
        migrations.RemoveField(
            model_name="stafftrainingru",
            name="parent",
        ),
        migrations.AlterModelOptions(
            name="staffscientificworks",
            options={
                "verbose_name": "Научный труд",
                "verbose_name_plural": "Научные труды",
            },
        ),
        migrations.AddField(
            model_name="stafftraining",
            name="description_en",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stafftraining",
            name="description_kg",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stafftraining",
            name="description_ru",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="StaffTrainingEN",
        ),
        migrations.DeleteModel(
            name="StaffTrainingKG",
        ),
        migrations.DeleteModel(
            name="StaffTrainingRU",
        ),
    ]
