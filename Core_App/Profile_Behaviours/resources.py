# resources.py
from import_export import resources
from .models import *

class SwipeResource(resources.ModelResource):
    class Meta:
        model = Swipes_Table

class MatchResource(resources.ModelResource):
    class Meta:
        model = Match_table

class StatusResource(resources.ModelResource):
    class Meta:
        model = UserStatus
