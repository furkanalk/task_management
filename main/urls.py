from django.urls import path
from .import views

urlpatterns = [
    # Task related functions
    path('tasks', views.showTaskList), # Show Task List
    path('tasks/<int:pk>', views.requestedTask), # Send a request to a Task
    path('tasks/add', views.addTask), # Add a new Task
    path('mytask', views.showMyTask), # Show Users their Task
    path('mytask/status', views.updateMyStatus), # Users can update their tasks' status
    
    # User related functions
    path('users', views.showUserList), # Show User List
    path('users/<int:pk>', views.requestedUser), # Send a request to a User
    path('users/add', views.addUser) # Add a new User
]