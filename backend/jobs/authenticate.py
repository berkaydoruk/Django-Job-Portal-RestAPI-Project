import jwt
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from users.models import User

class JWTAuthenticationCompany(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token is expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')

        user = get_object_or_404(User, id=payload['id'])

        if user.role != 'company':
            raise PermissionDenied('The role must be company')

        return (user, None)  
