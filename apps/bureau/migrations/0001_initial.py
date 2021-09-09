# Generated by Django 3.2.6 on 2021-09-08 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0033_auto_20210907_1704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bureau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=512)),
                ('title_ru', models.CharField(max_length=512, null=True)),
                ('title_ky', models.CharField(max_length=512, null=True)),
                ('title_en', models.CharField(max_length=512, null=True)),
                ('activities', models.TextField(verbose_name='Деятельность')),
                ('activities_ru', models.TextField(null=True, verbose_name='Деятельность')),
                ('activities_ky', models.TextField(null=True, verbose_name='Деятельность')),
                ('activities_en', models.TextField(null=True, verbose_name='Деятельность')),
                ('goal', models.TextField(verbose_name='Цель')),
                ('goal_ru', models.TextField(null=True, verbose_name='Цель')),
                ('goal_ky', models.TextField(null=True, verbose_name='Цель')),
                ('goal_en', models.TextField(null=True, verbose_name='Цель')),
                ('structure_title', models.CharField(blank=True, max_length=512, null=True)),
                ('structure_title_ru', models.CharField(blank=True, max_length=512, null=True)),
                ('structure_title_ky', models.CharField(blank=True, max_length=512, null=True)),
                ('structure_title_en', models.CharField(blank=True, max_length=512, null=True)),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
            },
        ),
        migrations.CreateModel(
            name='BureauTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('description_ru', models.TextField(null=True)),
                ('description_ky', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='bureau.bureau')),
            ],
        ),
        migrations.CreateModel(
            name='BureauMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=512, null=True)),
                ('position_ru', models.CharField(blank=True, max_length=512, null=True)),
                ('position_ky', models.CharField(blank=True, max_length=512, null=True)),
                ('position_en', models.CharField(blank=True, max_length=512, null=True)),
                ('specialist', models.BooleanField(default=False, verbose_name='Ведущий специалист?')),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='structure', to='bureau.bureau')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bureau_structure', to='staff.staff')),
            ],
        ),
        migrations.CreateModel(
            name='BureauContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('first_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('second_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True, verbose_name='Адрес')),
                ('bureau', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='bureau.bureau')),
            ],
        ),
    ]