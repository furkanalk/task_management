from authorization.models import User
from django.db import models

class Task(models.Model): 
    
    IDLE = 'idle'
    TODO = 'to Do'
    INPROGRESS = 'in Progress'
    DONE = 'Done'

    STATUS_CHOICES = (
        (IDLE, 'idle'),
        (TODO, 'to Do'),
        (INPROGRESS, 'in Progress'),
        (DONE, ' Done'),
    )
        
    task_name = models.CharField(max_length=50)
    task_description = models.TextField(max_length = 200)
    due_date = models.CharField(max_length = 30)
    assignee_name = models.CharField(max_length=20, blank=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=IDLE)
    
    class Meta:
        ordering = ('-status',)
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return self.task_name
    
    def get_user(self):
        return self.assignee