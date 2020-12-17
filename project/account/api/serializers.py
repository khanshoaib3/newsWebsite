from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from ..models import Profile, Photos


#=================================CreateUserSerializer=================================
class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    username = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    password = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    confirmPassword = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    firstName = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)

    def create(self, validated_data):
        if User.objects.filter(username = validated_data['username']).exists():
                return {'Error':'Username already exists!!'}
        else:
            if User.objects.filter(email = validated_data['email']).exists():
                return {'Error':'Email already exists!!'}
            else:
                if validated_data['password']==validated_data['confirmPassword']:
                    if len(validated_data['password']) >= 8:
                        specialCharachter = 0
                        number = 0
                        word = 0
                        for x in validated_data['password']:
                            if x=='!' or x=='@' or x=='#' or x=='^' or x=='&' or x=='*' or x=='#' or x=='(' or x==')' or x=='-' or x=='_' or x=='=' or x=='+' or x=='{' or x=='}' or x=='[' or x==']' or x=='|' or x=='\\' or x==';' or x==':' or x=='\'' or x=='"' or x=='<' or x=='>' or x==',' or x=='.' or x=='/' or x=='?' :
                                specialCharachter = specialCharachter + 1
                            if x>='0' and x<='9' :
                                number = number + 1
                            if (x>='a' and x<='z') or (x>='A' and x<='Z'):
                                word = word + 1
                        if specialCharachter > 0 and word > 0 and number > 0 :
                            u = User.objects.create_user(first_name=validated_data['firstName'],email=validated_data['email'],password=validated_data['password'],username=validated_data['username'])
                            Profile.objects.create(user=u)
                            token = Token.objects.get(user=u).key
                            return {'Token':token}
                        else:
                            return {'Error':'Password must contain a special charachter (@,!,#....), a number and an alphabet'}
                    else:
                        return {'Error':'Password too short, must be atleast 8 charachters long'}
                else:
                    return {'Error':'Password don\'t match'}
#======================================================================================


#=================================LoginUserSerializer==================================
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    password = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    
    def create(self, validated_data):
        user = authenticate(username=validated_data['username'],password=validated_data['password'])
        if user is not None :
            if user.is_active:
                token = Token.objects.get(user=user).key
                return {'Token':token}
            else :
                return {'Error':'account disabled'}
        else :
            return {'Error':'wrong credentials'}
#======================================================================================


#=================================EditUserPassSerializer===============================
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
                                return {'Error':'Cannot reuse previous password'}
                            else :
                                user.set_password(newPassword)
                                user.save()
                                return {'Status':'success' }
                        else:
                            return {'Error':'Password must contain a special charachter (@,!,#....), a number and an alphabet'}
                    else:
                        return {'Error':'Password too short, must be atleast 8 charachters long'}
                else :
                    return {'Error':'Passwords don\'t match'}
            else:
                 return {'Error':'Wrong Password'}
        except:
            return {'Error':'wrong token'}
#======================================================================================


#=================================EditUserProfileSerializer============================
class EditUserProfileSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    firstName = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    lastName = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    
    def create(self, validated_data):
        try:
            user = Token.objects.get(key=validated_data['token']).user
            user.first_name = validated_data['firstName']
            user.last_name = validated_data['lastName']
            user.save()
            return {'Error':'success'}
        except:
            return {'Error':'wrong token'}
#======================================================================================


#=================================DeleteUserSerializer=================================
class DeleteUserSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    oldpassword = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, write_only=True)
    
    def create(self, validated_data):
        try:
            user = Token.objects.get(key=validated_data['token']).user
            if user.check_password(validated_data['oldpassword']):
                user.delete()
                return {'Status':'success'}
            else:
                 return {'Error':'Wrong Password'}
        except:
            return {'Error':'wrong token'}
#======================================================================================



#=================================DeleteUserSerializer=================================
class PhotoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ('user', 'photo')
#======================================================================================