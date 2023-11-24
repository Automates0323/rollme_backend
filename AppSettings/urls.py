from unicodedata import name
from django.urls import path, include
from .views import *
from Functions.RestApi.RestApiRoutes import *
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework.authentication import SessionAuthentication

router = DefaultRouter()
router.register("UserExpectedApi", UserExpectedApi)
router.register("ProfessionApi", ProfessionApi)
router.register("IntresetedInApi", IntresetedInApi)
router.register("UserProfileApi", UserProfileApi)

urlpatterns = [
    path('core/', include(router.urls)),

    # Api Data's...
    path('login/', login_view, name="api-auth-login"),
    path('log_out/', log_out, name="api-auth-login"),

    path('profession/', getProfessions, name="profession"),
    path('expecting/', getExpect, name="expecting"),
    path('intrest/', getIntrests, name="profession"),

    path('createDummyUsers/', createDummyUsers, name="createDummyUsers"),


    # path('instruments/', getInstruments, name="instruments"),
    # path('auth/', authonticate, name="authonticate"),
    # path('optionchain/', updateOptionChain, name="updateOptionChain"),
    # path('api/', include(router.urls)),
    # path('admin/', admin.site.urls),
    # path('edith_api/', include('Edith_Algo.src.Api.urls')), 
    # path('token_update', updateAccessToken, name='update Token')
]