from rest_framework import serializers
from ..models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'role', 'password']
    
    def validate_role(self, value):
        valid_roles = {"applicant", "company"}
        
        if value not in valid_roles:
            raise serializers.ValidationError("The role must be applicant or company")
        return value

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)