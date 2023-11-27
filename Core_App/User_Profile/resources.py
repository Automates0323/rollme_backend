# resources.py
from import_export import resources
from .models import *
from django.contrib.auth.models import User


class GeolocationResource(resources.ModelResource):
    class Meta:
        model = Geolocation
