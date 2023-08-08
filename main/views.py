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
        Tasks = Task.objects.all().order_by('id')
        serializer = TaskSerializer(Tasks, many=True, context={'request': request})
        
    else:
        return HttpResponseNotAllowed(request.method)
    
    content = {'Tasks': serializer.data}
    return JsonResponse(content)

# Admin privilage
# Send a request to a Task
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def requestedTask(request,pk):
    theTask = get_object_or_404(Task, id=pk)
    
    if request.method == 'GET':
        serializer = TaskSerializer(theTask)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TaskSerializer(theTask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        name = theTask.task_name
        theTask.delete()
        return Response("Task named = " + str(name) + ", has been deleted.")
    
    else:
        return HttpResponseNotAllowed(request.method)

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
            return Response(serializer.errors)
    else:
        return HttpResponseNotAllowed(request.method)
    
# Admin privilage
# Show a list of all Users and their roles
@api_view(['GET'])
@permission_classes([IsAdminUser])
def showUserList(request):
    if request.method == 'GET':
        Users = User.objects.all().order_by('id')
        serializer = UserSerializer(Users, many=True, context={'request': request})
        
    else:
        return HttpResponseNotAllowed(request.method)
    
    content = {'Users': serializer.data}
    return JsonResponse(content)

# Admin privilage
# Send a request to a certain User
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def requestedUser(request,pk):
    theUser = get_object_or_404(User, id=pk)
    
    if request.method == 'GET':
        serializer = UserSerializer(theUser)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserUpdateSerializer(theUser, data=request.data)
        if serializer.is_valid():  
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    elif request.method == 'DELETE':
        theUser.delete()
        return Response("The User with ID NO = " + str(pk) + ", has been deleted.")
    
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
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
            return Response(serializer.errors)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Available for all Users
# Show Users their tasks. Also they can update it.
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
        return HttpResponseNotAllowed(request.method)
    
    if theTask is None:
        content = {'Your Task': 'You haven not assigned to a Task yet'}
    else:
        content = {'Your Task': serializer.data}
    return JsonResponse(content)

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
            return JsonResponse(content)
        else:
            return Response(serializer.errors)
        
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)