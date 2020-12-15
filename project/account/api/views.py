from rest_framework.decorators import api_view
from django.http import JsonResponse
from account.api.serializers import CreateUserSerializer, LoginUserSerializer, EditUserPassSerializer, EditUserProfileSerializer, DeleteUserSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



#================================hello_world===========================================
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return JsonResponse({"message": "Got some data!", "data": request.data})
    return JsonResponse({"message": "Hello, world!"})
#======================================================================================



#==============================createUserView==========================================
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def createUserView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreateUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)
#======================================================================================



#===============================loginUserView==========================================
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def loginUserView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)
#======================================================================================



#==============================editUserPassView========================================
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def editUserPassView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EditUserPassSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)
#======================================================================================



#=============================editUserProfileView======================================
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def editUserProfileView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EditUserProfileSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)
#======================================================================================



#================================deleteUserView========================================
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def deleteUserView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeleteUserSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)
#======================================================================================


