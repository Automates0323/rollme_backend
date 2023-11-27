from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User
from .models import *
from .resources import *


@admin.register(Swipes_Table)
class Swipes_TableAdmin(ImportExportModelAdmin):
    resource_class = SwipeResource
    list_display = ("owner", "swiper_user_id", "swiped_direction")
    list_display_list = ("owner", "swiper_user_id", "swiped_direction")


@admin.register(Match_table)
class Match_tableAdmin(ImportExportModelAdmin):
    resource_class = MatchResource
    list_display = ("user1_id", "user2_id", "time_stamp")
    list_display_list = ("user1_id", "user2_id", "time_stamp")


@admin.register(UserStatus)
class Status_tableAdmin(ImportExportModelAdmin):
    resource_class = StatusResource
    list_display = ("user", "status_text", "status_image", "timestamp")
    list_display_list = ("user", "status_text", "status_image", "timestamp")
