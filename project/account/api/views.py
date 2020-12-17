from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from account.api.serializers import CreateUserSerializer, LoginUserSerializer, EditUserPassSerializer, EditUserProfileSerializer, DeleteUserSerializer, PhotoUploadSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from account.models import Photos



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




#================================deleteUserView========================================
class photoUploadView(ListAPIView):
    def get(self, request):
        queryset = Photos.objects.filter(user=request.user)
        serializer_class = PhotoUploadSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)

    def post(self, request):
        file1 = request.data['file']
        image = Photos.objects.create(photo=file1,user=request.user)
        serializer_class = PhotoUploadSerializer(image)
        return JsonResponse(serializer_class.data, safe=False)
    
    def delete(self, request):
        photo = Photos.objects.filter(pk=request.data['pk'])
        photo.delete()
        return JsonResponse({'status':'success'})
#======================================================================================