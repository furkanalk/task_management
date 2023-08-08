from authorization.models import User
from rest_framework import serializers
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email' , 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'required': True}
        }
        
    def create(self, validated_data):
        user = User(username = validated_data['username'], email = validated_data['email'], role = validated_data['role'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        extra_kwargs = {
            'role': {'required': True}
        }
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'task_description', 'due_date', 'assignee' , 'status']

class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']