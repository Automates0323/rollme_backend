# Generated by Django 4.2.2 on 2023-11-22 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Swipes_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swiped_direction', models.IntegerField(blank=True, null=True)),
                ('time_stamp', models.DateField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_owner', to=settings.AUTH_USER_MODEL)),
                ('swiper_user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_swipped', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Swipes Table',
                'verbose_name_plural': 'Swipes Table',
            },
        ),
        migrations.CreateModel(
            name='Match_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateField(default=django.utils.timezone.now)),
                ('user1_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user1_matches', to=settings.AUTH_USER_MODEL)),
                ('user2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2_matches', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Match Table',
                'verbose_name_plural': 'Match Table',
            },
        ),
    ]