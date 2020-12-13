from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return JsonResponse({"message": "Got some data!", "data": request.data})
    return JsonResponse({"message": "Hello, world!"})