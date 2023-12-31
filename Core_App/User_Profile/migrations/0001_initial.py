# Generated by Django 4.2.7 on 2023-11-24 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppSettings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('canShowGender', models.BooleanField(default=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='userprofile/')),
                ('profile_banner', models.ImageField(blank=True, null=True, upload_to='userbanner/')),
                ('canShowUserProfession', models.BooleanField(default=True)),
                ('canShowUserIntresetedIn', models.BooleanField(default=True)),
                ('canShowUserExpected', models.BooleanField(default=True)),
                ('IntresetedIn', models.ManyToManyField(blank=True, null=True, to='AppSettings.intresetedin')),
                ('UserExpected', models.ManyToManyField(blank=True, null=True, to='AppSettings.userexpected')),
                ('UserProfession', models.ManyToManyField(blank=True, null=True, to='AppSettings.userprofession')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profile',
            },
        ),
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
