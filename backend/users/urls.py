from django.urls import path
from .views import *

user_patterns = [
    path('api/users/register/', UserRegistrationApi.as_view(), name='user-register'),
    path('api/users/login/', UserLoginApi.as_view(), name='user-login'),
    #path('api/users/refresh-token/', RefreshTokenApi.as_view(), name='refresh-token'),
    path('api/users/logout/', LogoutApi.as_view(), name='user-logout'),
]


urlpatterns = user_patterns