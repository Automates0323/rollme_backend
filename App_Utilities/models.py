from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PushNotifications(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_notif')
    to_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='about_user')
    title = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    read_status = models.BooleanField(default=False)
    time_stamp = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Match between {self.user1_id} and {self.user2_id}"
    class Meta:
        verbose_name = 'Notifications'
        verbose_name_plural = 'Notifications'