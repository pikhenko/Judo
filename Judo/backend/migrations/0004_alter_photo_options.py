# Generated by Django 4.2.2 on 2023-08-17 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_comment_body_alter_comment_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['time_create'], 'verbose_name': 'Фотографии', 'verbose_name_plural': 'Фотографии'},
        ),
    ]