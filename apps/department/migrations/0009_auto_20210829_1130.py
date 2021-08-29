# Generated by Django 3.2.6 on 2021-08-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0008_auto_20210829_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='description',
            field=models.TextField(verbose_name='Информация о кафедре'),
        ),
        migrations.AlterField(
            model_name='department',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Информация о кафедре'),
        ),
        migrations.AlterField(
            model_name='department',
            name='description_ky',
            field=models.TextField(null=True, verbose_name='Информация о кафедре'),
        ),
        migrations.AlterField(
            model_name='department',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Информация о кафедре'),
        ),
    ]
