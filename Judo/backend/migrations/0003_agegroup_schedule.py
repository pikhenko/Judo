# Generated by Django 2.2.19 on 2023-09-28 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20230914_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Возраст',
                'verbose_name_plural': 'Возраст',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('address', models.CharField(default='DEFAULT VALUE', max_length=100, verbose_name='Адрес')),
                ('age_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.AgeGroup')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
    ]