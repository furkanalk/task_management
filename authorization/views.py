from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotAllowed, HttpResponse
from django.contrib.auth import authenticate
from django.conf import settings
#
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
#
from main.serializer import UserSerializer
from .models import User
import requests

# Register
@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# Login
@api_view(['POST'])
@permission_classes([AllowAny])
def loginUser(request):
    if request.method == 'POST':
        usern = request.data.get('username')
        passw = request.data.get('password')

        user = None
        if '@' in usern:
            try:
                user = User.objects.get(email=usern)
            except ObjectDoesNotExist:
                raise AuthenticationFailed('User NOT found.')

        if not user:
            user = authenticate(username=usern, password=passw)
        
        url = 'http://localhost:8000/o/token/'
        payload = {'grant_type': 'password',
                   'username': usern,
                   'password': passw,
                   'Content-type': 'application/x-www-form-urlencoded',
                   'client_id': settings.CLIENT_ID,
                   'client_secret': settings.CLIENT_SECRET}
        result = requests.post(url, data=payload)
        
        if user:
            return HttpResponse(result, status=status.HTTP_200_OK)
                  
        return Response({'error': 'Username or password is incorrect.'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)