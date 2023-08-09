from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
#
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
#
from authorization.models import User
from .serializer import UserSerializer, UserUpdateSerializer, TaskSerializer, TaskStatusSerializer
from .models import Task
#from django.contrib.auth.hashers import make_password

# Admin privilage
# Show a list of all Tasks (detailed) and who assigned to them
@api_view(['GET'])
@permission_classes([IsAdminUser])
def showTaskList(request):
    if request.method == 'GET':
        try:
            Tasks = Task.objects.all().order_by('id')
        except:
            Tasks = None
        
        if Tasks == None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(Tasks, many=True, context={'request': request})
        
        content = {'Tasks': serializer.data}
    else:
        return Response(request.method, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    return Response(content, status=status.HTTP_200_OK)

# Admin privilage
# Send a request to a Task
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def requestedTask(request,pk):
    theTask = get_object_or_404(Task, id=pk)
    
    if request.method == 'GET':
        serializer = TaskSerializer(theTask)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(theTask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        name = theTask.task_name
        theTask.delete()
        return Response("Task named = " + str(name) + ", has been deleted.", status=status.HTTP_200_OK)
    
    else:
        return Response(request.method, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# Admin privilage
# Add a new Task 
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addTask(request):     
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(request.method, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
# Admin privilage
# Show a list of all Users and their roles
@api_view(['GET'])
@permission_classes([IsAdminUser])
def showUserList(request):
    if request.method == 'GET':
        Users = User.objects.all().order_by('id')
        try:
            serializer = UserSerializer(Users, many=True, context={'request': request})
        except:
            serializer = None
            
        content = {'Users': serializer.data}
    else:
        return Response(request.method, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    if serializer == None:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    return Response(content, status=status.HTTP_200_OK)

# Admin privilage
# Send a request to a certain User
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def requestedUser(request,pk):
    theUser = get_object_or_404(User, id=pk)
    
    if request.method == 'GET':
        try:
            serializer = UserSerializer(theUser)
        except:
            serializer = None
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        try:
            serializer = UserUpdateSerializer(theUser, data=request.data)
        except:
            serializer = None
            return Response("User information changed successfully",status=status.HTTP_404_NOT_FOUND)
        
        if serializer.is_valid():  
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':    
        theUser.delete()
        return Response("The User with ID NO = " + str(pk) + ", has been deleted.", status=status.HTTP_200_OK)
    
    else:
        return Response(request.method, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
# Admin privilage
# Add a new User 
@api_view(['POST'])
@permission_classes([IsAdminUser])
def addUser(request):     
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(request.method, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# Available for all Users
# Show Users their tasks.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showMyTask(request):
    if request.method == 'GET':
        try:
            theTask = Task.objects.get(assignee = request.user.id)
        except:
            theTask = None    
        serializer = TaskSerializer(theTask, context={'request': request})   
    else:
        return Response(request.method, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    if theTask is None:
        content = {'Your Task': 'You haven not assigned to a Task yet'}
    else:
        content = {'Your Task': serializer.data}
        
    return Response(content, status=status.HTTP_200_OK)

# Available for all Users
# Users can update their tasks' status
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMyStatus(request):
    if request.method == 'PUT':
        theTask = get_object_or_404(Task, assignee = request.user.id)
        serializer = TaskStatusSerializer(theTask, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            content = {'Your Status': serializer.data}
            return Response(content, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)