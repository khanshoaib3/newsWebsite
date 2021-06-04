from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from newsBlog.api.serializers import GetPostSerializer, CreatePostSerializer, EditPostSerializer, DeletePostSerializer
from rest_framework.decorators import authentication_classes, permission_classes


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def getPostView(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        serializer = GetPostSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse({"data":list(data)})
        return JsonResponse(serializer.errors, status=400)



@api_view(['POST','PUT','DELETE'])
def editPostView(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CreatePostSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EditPostSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        data = JSONParser().parse(request)
        serializer = DeletePostSerializer(data=data)
        if serializer.is_valid():
            data = serializer.create(data)
            return JsonResponse(data)
        return JsonResponse(serializer.errors, status=400)