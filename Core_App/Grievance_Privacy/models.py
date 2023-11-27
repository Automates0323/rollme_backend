from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class BlockedUsers(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_blocked')
    blocked_user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='blocked_user')
    block_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Blocked Users by {self.user_id} on {self.user_id}"

    class Meta:
        verbose_name = 'Blocked Users'
        verbose_name_plural = 'Blocked Users'
    
class ReportUser(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_reported')
    reported_user_id  = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reported_user_id')
    report_reason = models.CharField(max_length=255, null=True, blank=True)
    report_sub_reason = models.CharField(max_length=255, null=True, blank=True)
    report_note = models.TextField(null=True, blank=True)
    report_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Reported Users by {self.user_id} on {self.user_id}"

    class Meta:
        verbose_name = 'Reported User'
        verbose_name_plural = 'Report Users'

class User_Settings(models.Model):
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='User_Settings')
    notification_enabled = models.BooleanField(default=True, null=True)
    theme = models.CharField(max_length=255, default="Light", blank=True, null=True)
    privacy_level = models.CharField(max_length=255, default="Private", blank=True, null=True)
    language = models.CharField(max_length=255, default="ENG", blank=True, null=True)
    email_notification_enabled = models.BooleanField(default=True)
    push_notification_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"ettings Users by {self.user_id} on {self.user_id}"

    class Meta:
        verbose_name = 'User Settings'
        verbose_name_plural = 'App Settings'