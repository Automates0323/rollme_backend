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

@api_view(['POST', ])
@permission_classes((AllowAny,))
def login_view(request):
    try:
        requestData = json.loads(request.body)
        token = requestData.get('crypto')
        
        if token is None:
            return JsonResponse({
                "errors": {
                    "detail": "Please provide a valid JWT token"
                }
            }, status=400)

        data = JWTEncriptions.decode_jwt(token)

        if data is not None:
            username = data.get('username')
            password = data.get('password')

            if username is None or password is None:
                return JsonResponse({
                    "errors": {
                        "detail": "Invalid token data"
                    }
                }, status=400)

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                userProfile = User_Profile.objects.filter(user_id=request.user)
                serializer = User_ProfileSerializer(userProfile, many=True)

                # Serialize data to JSON
                serialized_data = json.dumps(serializer.data)

                # Encode a new JWT token with the serialized data in the payload
                response_token = JWTEncriptions.encode_jwt({"user_data": serialized_data})

                response_data = {
                    "status": 200,
                    "token": response_token,
                    "message": "Login successful"
                }
                return JsonResponse(response_data)
            else:
                return JsonResponse(
                    {"errors": "Invalid credentials"},
                    status=400,
                )
        else:
            return JsonResponse(
                {"errors": "Invalid JWT token"},
                status=400,
            )

    except Exception as e:
        print("Invalid Data Input...")
        return JsonResponse(
            {"errors": "An error occurred"},
            status=500,
        )


@api_view(['POST', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def log_out(request):
    # Dispatch the signal before the user is logged out so the receivers have a
    # chance to find out *who* logged out.
    user = getattr(request, 'user', None)
    if user and user.is_authenticated:
        user = None
        user_logged_out.send(sender=user.__class__, request=request, user=user)

    request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()

    return JsonResponse({"detail": "Logout successful"})


@api_view(['GET', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def getProfessions(request):
    try:
        professions = UserProfession.objects.all()
    except UserProfession.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = UserProfessionSerializer(professions, many=True)
        return Response({"status":200, "data":serializers.data})
    

@api_view(['GET', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def getIntrests(request):
    try:
        intrest = IntresetedIn.objects.all()
    except IntresetedIn.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = IntresetedInSerializer(intrest, many=True)
        return Response({"status":200, "data":serializers.data})
    
@api_view(['GET', ])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def getExpect(request):
    try:
        expected = UserExpected.objects.all()
    except UserExpected.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = UserExpectedSerializer(expected, many=True)
        return Response({"status":200, "data":serializers.data})


@api_view(['POST', ])
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
        create = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        print(create)
    return Response({"status":200, "data":"Success"})