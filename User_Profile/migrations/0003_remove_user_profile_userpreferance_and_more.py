# Generated by Django 4.2.2 on 2023-11-22 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0002_alter_user_profile_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='UserPreferance',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='canShowUserPreferance',
        ),
    ]
