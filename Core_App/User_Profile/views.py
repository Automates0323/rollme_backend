from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from Functions.RestApi.JSONSerializers import *
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.contrib.auth.signals import user_logged_out
import json
from Functions.MatchScore.Score import *
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def getProfile(request):
    try:
        userProfile = User_Profile.objects.filter(user_id=request.user)
    except User_Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = User_ProfileSerializer(userProfile, many=True)
        return Response({"status":200, "data":serializers.data})
    
@api_view(['POST', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def getmatch(request):
    calculatedScore = calculate_match_scores(request.user)
    return Response({"status":200, "data":calculatedScore})