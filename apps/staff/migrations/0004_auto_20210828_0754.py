# Generated by Django 3.2.6 on 2021-08-28 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_staffeducation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffeducation',
            name='description',
        ),
        migrations.CreateModel(
            name='StaffEducationRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ru', to='staff.staffeducation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffEducationKG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kg', to='staff.staffeducation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StaffEducationEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='en', to='staff.staffeducation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
