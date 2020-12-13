from rest_framework.decorators import api_view
from django.http import JsonResponse
from account.api.serializers import CreateUserSerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return JsonResponse({"message": "Got some data!", "data": request.data})
    return JsonResponse({"message": "Hello, world!"})
//comment
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def createUserView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreateUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.get(user=user).key
            return JsonResponse({'Token':token})
        return JsonResponse(serializer.errors, status=400)