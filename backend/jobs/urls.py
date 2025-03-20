from django.urls import path
from .views import *

user_patterns = [
    path('api/company/register/', CompanyRegistrationApi.as_view(), name='company-register'),
    path('api/company/detail/', CompanyDetailApi.as_view(), name='company-detail'),
]


urlpatterns = user_patterns