from unicodedata import name
from django.urls import path, include
from .views import *
from Functions.RestApi.RestApiRoutes import *
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authentication import SessionAuthentication

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user_profile/', getProfile, name="user_profile"),
    path('match_profile/', getmatch, name="match_profile"),
]
