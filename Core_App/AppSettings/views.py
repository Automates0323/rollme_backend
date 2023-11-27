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
from Functions import JWTEncriptions
from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
# Create your views here.

import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET', ])
@permission_classes((AllowAny,))
@csrf_exempt
def getProfessions(request):
    try:
        professions = UserProfession.objects.all()
    except UserProfession.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = UserProfessionSerializer(professions, many=True)
        return Response({"status": 200, "data": serializers.data})


@api_view(['GET', ])
@permission_classes((AllowAny,))
@csrf_exempt
def getIntrests(request):
    try:
        intrest = IntresetedIn.objects.all()
    except IntresetedIn.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = IntresetedInSerializer(intrest, many=True)
        return Response({"status": 200, "data": serializers.data})


@api_view(['GET', ])
@permission_classes((AllowAny,))
@csrf_exempt
def getExpect(request):
    try:
        expected = UserExpected.objects.all()
    except UserExpected.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = UserExpectedSerializer(expected, many=True)
        return Response({"status": 200, "data": serializers.data})


@api_view(['GET', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def createDummyUsers(request):
    fake = Faker()
    total_users = 10
    for _ in range(total_users):
        # Generate random data
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        first_name = fake.first_name()
        last_name = fake.last_name()
        # Create the user
        create = User.objects.create_user(
            username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        print(create)
    return Response({"status": 200, "data": "Success"})
