from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class UserProfession(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    icons = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'User Profession'
        verbose_name_plural = 'User Profession'

class IntresetedIn (models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    icons = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'User Intrested'
        verbose_name_plural = 'User Intrested'

class UserExpected(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    descriptions = models.CharField(max_length=255, null=True, blank=True)
    icons = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'User Expected'
        verbose_name_plural = 'User Expected'