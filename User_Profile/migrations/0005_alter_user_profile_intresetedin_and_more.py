# Generated by Django 4.2.2 on 2023-11-22 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSettings', '0006_delete_userpreferance'),
        ('User_Profile', '0004_user_profile_profile_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='IntresetedIn',
            field=models.ManyToManyField(blank=True, null=True, to='AppSettings.intresetedin'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='UserExpected',
            field=models.ManyToManyField(blank=True, null=True, to='AppSettings.userexpected'),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='UserProfession',
            field=models.ManyToManyField(blank=True, null=True, to='AppSettings.userprofession'),
        ),
    ]
