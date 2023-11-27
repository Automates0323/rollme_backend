from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Swipes_Table(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,  related_name='user_owner')
    swiper_user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user_swipped')
    swiped_direction = models.IntegerField(null=True, blank=True)
    time_stamp = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Swipes by {self.owner} on {self.swiper_user_id}"

    class Meta:
        verbose_name = 'Swipes'
        verbose_name_plural = 'Swipes'

class Match_table(models.Model):
    user1_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user1_matches')
    user2_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user2_matches')
    is_mutual = models.BooleanField(default=False, blank=True, null=True)
    time_stamp = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Match between {self.user1_id} and {self.user2_id}"
    class Meta:
        verbose_name = 'Matches'
        verbose_name_plural = 'Matches'


class UserStatus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_text = models.TextField(blank=True)
    status_image = models.ImageField(upload_to='status_images/', null=True, blank=True)
    status_video = models.FileField(upload_to='status_videos/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Status between {self.user} and {self.status_text}"
    class Meta:
        verbose_name = 'User Status'
        verbose_name_plural = 'User Status'
