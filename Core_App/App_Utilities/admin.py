from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from .models import *
from .resources import *

# Register your models here.


@admin.register(PushNotifications)
class Notifications_Admin(ImportExportModelAdmin):
    resource_class = NotificationsResource
    list_display = ("user_id", "to_user", "message", "time_stamp")
    list_display_list = ("user_id", "to_user", "message", "time_stamp")
