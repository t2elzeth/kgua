# Generated by Django 3.2.6 on 2021-08-27 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='DepartmentRU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('salary', models.CharField(max_length=255)),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ru', to='department.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentKG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('salary', models.CharField(max_length=255)),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kg', to='department.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentEN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('salary', models.CharField(max_length=255)),
                ('parent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='en', to='department.department')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]