from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from .models import * 
from .resources import *

# Register your models here.
@admin.register(BlockedUsers)
class BlockedUsersAdmin(ImportExportModelAdmin):
    resource_class = BlockedResource
    list_display = ("user_id", "blocked_user_id", "block_date")
    list_display_list  = ("user_id", "blocked_user_id", "block_date")

@admin.register(ReportUser)
class BlockedUsersAdmin(ImportExportModelAdmin):
    resource_class = ReportResource
    list_display = ("user_id", "reported_user_id", "report_reason")
    list_display_list  = ("user_id", "reported_user_id", "report_reason")

@admin.register(User_Settings)
class BlockedUsersAdmin(ImportExportModelAdmin):
    resource_class = SettingsResource
    list_display = ("user_id", "notification_enabled", "theme")
    list_display_list  = ("user_id", "notification_enabled", "theme")