from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
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
                response_token = JWTEncriptions.encode_jwt(
                    {"user_data": serialized_data})

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
@permission_classes((AllowAny,))
def signup(request):
    if request.method == 'POST':
        requestData = json.loads(request.body)

        username = requestData.get('username')
        password = requestData.get('password')
        first_name = requestData.get('first_name')
        last_name = requestData.get('last_name')

        # Validate required fields
        if not username or not password:
            return JsonResponse({'error': 'Username and password are required fields'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)

        if user:
            return JsonResponse({'status': 200, "data":"Success"}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'error': 'Failed to register user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST',])
@permission_classes[(AllowAny), ]
def validate_user(request):
    pass

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
