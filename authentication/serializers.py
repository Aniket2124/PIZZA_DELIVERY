from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from .models import User


class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number']

        def validate(self, attrs):
            if User.objects.filter(username=attrs['username']).exists():
                raise serializers.ValidationError('Username already exists')
            
            if User.objects.filter(email=attrs['email']).exists():
                raise serializers.ValidationError('Email already exists')
            
            if User.objects.filter(phone_number=attrs['phone_number']).exists():
                raise serializers.ValidationError('Phone number already exists')
            
            return super().validate(attrs)
         