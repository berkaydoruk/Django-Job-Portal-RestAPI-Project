import jwt, datetime
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.auth_serializers import *

class UserRegistrationApi(GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            response_data = {
                    "message": "User has been created successfully.",
                    "id": user.id,
                    "e-mail": user.email,
                    "phone_number": user.phone_number,
                    "role": user.role,
                }

            
            return Response(response_data, status=status.HTTP_201_CREATED)

        errors = {key: " ".join(value) for key, value in serializer.errors.items()}
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginApi(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Username and password are required'}, status=400)

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(
            key='jwt',
            value=token,
            httponly=True,
            samesite='None',
            secure=True,  
        )

        user.last_login = datetime.datetime.now()
        user.is_online = True
        user.save()

        response.data = [{
            'jwt': token,
            'email': user.email,
            'role': user.role
        }]

        return response
        
class LogoutApi(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')

        token = request.COOKIES.get('jwt')
        if token is None:
            return Response({'AuthenticationFailed': 'You are already not logged in.'}, status=401)
        
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        user = User.objects.get(id=payload['id'])
        user.is_online = False

        response.data = {
            'message': 'Logged out successfully.',
        }
        return response
        
