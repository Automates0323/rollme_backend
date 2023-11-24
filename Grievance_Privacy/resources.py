# resources.py
from import_export import resources
from .models import *

class BlockedResource(resources.ModelResource):
    class Meta:
        model = BlockedUsers

class ReportResource(resources.ModelResource):
    class Meta:
        model = ReportUser

class SettingsResource(resources.ModelResource):
    class Meta:
        model = User_Settings