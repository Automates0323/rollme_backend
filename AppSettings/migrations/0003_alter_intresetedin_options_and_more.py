# Generated by Django 4.2.2 on 2023-11-21 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSettings', '0002_alter_intresetedin_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='intresetedin',
            options={'verbose_name': 'User Intrested In', 'verbose_name_plural': 'User Intrested In'},
        ),
        migrations.AlterModelOptions(
            name='userexpected',
            options={'verbose_name': 'User Expected', 'verbose_name_plural': 'User Expected'},
        ),
        migrations.AlterModelOptions(
            name='userpreferance',
            options={'verbose_name': 'User Preferance', 'verbose_name_plural': 'User Preferance'},
        ),
        migrations.AlterModelOptions(
            name='userprofession',
            options={'verbose_name': 'User Profession', 'verbose_name_plural': 'User Profession'},
        ),
    ]
