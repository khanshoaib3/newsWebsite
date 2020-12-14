from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password','first_name',]
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required':True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.first_name = validated_data['first_name']
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    password = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    
    def create(self, validated_data):
        user = authenticate(username=validated_data['username'],password=validated_data['password'])
        if user is not None :
            if user.is_active:
                token = Token.objects.get(user=user).key
                return token
            else :
                return 'account disabled'
        else :
            return 'wrong credentials'