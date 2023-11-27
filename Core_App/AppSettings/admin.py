from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *
# Register your models here.


@admin.register(UserProfession)
class UserProfessionAdmin(ImportExportModelAdmin):
    resource_class = UserProfessionResource
    list_display = ("id", "title")
    list_display_list = ("id", "title")


@admin.register(IntresetedIn)
class IntresetedInAdmin(ImportExportModelAdmin):
    resource_class = UserIntresetedInResource
    list_display = ("id", "title")
    list_display_list = ("id", "title")


@admin.register(UserExpected)
class UserExpectedAdmin(ImportExportModelAdmin):
    resource_class = UserExpectedResource
    list_display = ("id", "title")
    list_display_list = ("id", "title")
