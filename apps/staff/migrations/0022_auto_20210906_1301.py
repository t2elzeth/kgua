# Generated by Django 3.2.6 on 2021-09-06 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0021_alter_staff_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='position_en',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='position_ky',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='position_ru',
            field=models.CharField(max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='staffeducation',
            name='from_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Начиная с'),
        ),
        migrations.AlterField(
            model_name='staffeducation',
            name='to_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='До'),
        ),
    ]
