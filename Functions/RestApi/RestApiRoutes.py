from User_Profile.models import *
from Functions.RestApi.JSONSerializers import * 
from rest_framework import viewsets
from rest_framework.response import Response
from LiveChats.models import *
from Profile_Behaviours.models import *
from User_Profile.models import *
from AppSettings.models import *
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class ProfessionApi(viewsets.ModelViewSet):
    queryset = UserProfession.objects.all()
    serializer_class = UserProfessionSerializer

class IntresetedInApi(viewsets.ModelViewSet):
    queryset = IntresetedIn.objects.all()
    serializer_class = IntresetedInSerializer

class UserExpectedApi(viewsets.ModelViewSet):
    queryset = UserExpected.objects.all()
    serializer_class = UserExpectedSerializer

class UserProfileApi(viewsets.ModelViewSet):
    queryset = User_Profile.objects.all()
    serializer_class = User_ProfileSerializer