from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from .models import * 
from .resources import *

@admin.register(Geolocation)
class GeolocationAdmin(ImportExportModelAdmin):
    resource_class = GeolocationResource
    list_display = ("id", "latitude")
    list_display_list  = ("id", "longitude")