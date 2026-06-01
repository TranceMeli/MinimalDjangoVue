from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def home(request):
    return Response({'message': 'Hello from Home API'})

@api_view(['GET'])
def about(request):
    return Response({'message': 'Hello from About'})

@api_view(['GET'])
def projects(request):
    return Response({'message': 'Hello from Projects'})

@api_view(['GET'])
def contact(request):
    return Response({'message': 'Hello from Contact'})