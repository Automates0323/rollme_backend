from django.db import models
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User
from AppSettings.models import *
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from import_export.admin import ImportExportModelAdmin


class User_Profile(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    canShowGender = models.BooleanField(default=True)
    profile_picture = models.ImageField(
        upload_to='userprofile/', null=True, blank=True)
    profile_banner = models.ImageField(
        upload_to='userbanner/', null=True, blank=True)

    UserProfession = models.ManyToManyField(
        UserProfession, null=True, blank=True)
    canShowUserProfession = models.BooleanField(default=True)

    IntresetedIn = models.ManyToManyField(IntresetedIn, null=True, blank=True)
    canShowUserIntresetedIn = models.BooleanField(default=True)

    UserExpected = models.ManyToManyField(UserExpected, null=True, blank=True)
    canShowUserExpected = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profile'


class User_ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = '__all__'  # Include all fields from the model
        widgets = {
            'UserProfession': FilteredSelectMultiple('UserProfession', is_stacked=False),
            'IntresetedIn': FilteredSelectMultiple('IntresetedIn', is_stacked=False),
            'UserExpected': FilteredSelectMultiple('UserExpected', is_stacked=False),
        }


class User_ProfileAdmin(ImportExportModelAdmin):
    form = User_ProfileAdminForm
    list_display = ("id", "user_id", "dob", "gender", "canShowGender",
                    "get_user_profession_display", "canShowUserIntresetedIn", "canShowUserExpected")

    def get_user_profession_display(self, obj):
        return ', '.join([str(up) for up in obj.UserProfession.all()])

    get_user_profession_display.short_description = 'UserProfession'


# Register the models and admin class
admin.site.register(User_Profile, User_ProfileAdmin)


# Geo Locations.........
class Geolocation(models.Model):
    user_id = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=255, blank=True, null=True)
