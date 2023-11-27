from import_export import resources
from .models import *

class NotificationsResource(resources.ModelResource):
    class Meta:
        model = PushNotifications