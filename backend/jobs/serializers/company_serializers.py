from rest_framework import serializers
from ..models import Company

class CompanyRegistrationSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Company
        fields = ['owner', 'company_name', 'company_country', 'company_city', 'company_industry', 'company_website']
    
    