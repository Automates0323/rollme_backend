# Generated by Django 4.2.2 on 2023-11-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSettings', '0004_alter_intresetedin_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intresetedin',
            name='icons',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userexpected',
            name='icons',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userpreferance',
            name='icons',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofession',
            name='icons',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
