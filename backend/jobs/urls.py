from django.urls import path
from .views import *

user_patterns = [
    path('api/company/register/', CompanyRegistrationApi.as_view(), name='company-register'),
]


urlpatterns = user_patterns