import jwt, datetime
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from ..authenticate import JWTAuthenticationCompany
from ..serializers.company_serializers import *

class CompanyRegistrationApi(GenericAPIView):
    authentication_classes = [JWTAuthenticationCompany]
    permission_classes = [IsAuthenticated]
    serializer_class = CompanyRegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(owner=request.user)

            response_data = {
                "message": "Company registered successfully!",
                "company": serializer.data 
            }

            return Response(response_data, status=status.HTTP_201_CREATED)

        errors = {key: " ".join(value) for key, value in serializer.errors.items()}
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
