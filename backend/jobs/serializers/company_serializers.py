from rest_framework import serializers
from ..models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'company_country', 'company_city', 'company_industry', 'company_website']

class CompanyRegistrationSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Company
        fields = ['owner', 'company_name', 'company_country', 'company_city', 'company_industry', 'company_website']
    
    def validate(self, value):
        if Company.objects.filter(owner=self.context['request'].user).exists():
            raise serializers.ValidationError("You can register only one company.")
        return value