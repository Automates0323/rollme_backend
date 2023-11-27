from rest_framework import serializers
from LiveChats.models import *
from Profile_Behaviours.models import *
from User_Profile.models import *
from AppSettings.models import *
from django.contrib.auth.models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfession
        fields = "__all__"

class IntresetedInSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntresetedIn
        fields = "__all__"

class UserExpectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExpected
        fields = "__all__"

from rest_framework import serializers

class User_ProfileSerializer(serializers.ModelSerializer):
    user_id = UsersSerializer(read_only=True)
    UserProfession = UserProfessionSerializer(many=True, read_only=True)
    IntresetedIn = IntresetedInSerializer(many=True, read_only=True)
    UserExpected = UserExpectedSerializer(many=True, read_only=True)

    class Meta:
        model = User_Profile
        fields = "__all__"
