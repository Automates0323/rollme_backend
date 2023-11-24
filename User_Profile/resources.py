# resources.py
from import_export import resources
from .models import *

class GeolocationResource(resources.ModelResource):
    class Meta:
        model = Geolocation
