# resources.py
from import_export import resources
from .models import *
from User_Profile.models import *

class UserExpectedResource(resources.ModelResource):
    class Meta:
        model = UserExpected
        # You can customize fields or exclude them if needed
        # fields = ('field1', 'field2',)

class UserProfessionResource(resources.ModelResource):
    class Meta:
        model = UserProfession
        # You can customize fields or exclude them if needed
        # fields = ('field1', 'field2',)

class UserIntresetedInResource(resources.ModelResource):
    class Meta:
        model = IntresetedIn
        # You can customize fields or exclude them if needed
        # fields = ('field1', 'field2',)

class UserProfileResource(resources.ModelResource):
    class Meta:
        model = User_Profile
