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

class EditUserPassSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    oldpassword = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    newpassword = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    confirmpassword = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    
    def create(self, validated_data):
        try:
            user = Token.objects.get(key=validated_data['token']).user
            if user.check_password(validated_data['oldpassword']):
                newPassword = validated_data['newpassword']
                confirmNewPassword = validated_data['confirmpassword']
                if newPassword==confirmNewPassword:
                    if len(newPassword) >= 8:
                        specialCharachter = 0
                        number = 0
                        word = 0
                        for x in newPassword:
                            if x=='!' or x=='@' or x=='#' or x=='^' or x=='&' or x=='*' or x=='#' or x=='(' or x==')' or x=='-' or x=='_' or x=='=' or x=='+' or x=='{' or x=='}' or x=='[' or x==']' or x=='|' or x=='\\' or x==';' or x==':' or x=='\'' or x=='"' or x=='<' or x=='>' or x==',' or x=='.' or x=='/' or x=='?' :
                                specialCharachter = specialCharachter + 1
                            if x>='0' and x<='9' :
                                number = number + 1
                            if (x>='a' and x<='z') or (x>='A' and x<='Z'):
                                word = word + 1
                        if specialCharachter > 0 and word > 0 and number > 0 :
                            if user.check_password(newPassword):
                                return 'Cannot reuse previous password'
                            else :
                                user.set_password(newPassword)
                                user.save()
                                return 'success' 
                        else:
                            return 'Password must contain a special charachter (@,!,#....), a number and an alphabet'
                    else:
                        return 'Password too short, must be atleast 8 charachters long'
                else :
                    return 'Passwords don\'t match'
            else:
                 return 'Wrong Password'
        except:
            return 'wrong token'
        