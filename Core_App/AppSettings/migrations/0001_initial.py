# Generated by Django 4.2.7 on 2023-11-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntresetedIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('icons', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'User Intrested',
                'verbose_name_plural': 'User Intrested',
            },
        ),
        migrations.CreateModel(
            name='UserExpected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('icons', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'User Expected',
                'verbose_name_plural': 'User Expected',
            },
        ),
        migrations.CreateModel(
            name='UserProfession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True)),
                ('icons', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'User Profession',
                'verbose_name_plural': 'User Profession',
            },
        ),
    ]
