from rest_framework.response import Response

from user.models import MyUser
from django.db import models
from datetime import datetime
# Create your models here.

class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)






class TaskList(models.Model):
    objects = TaskListManager()
    name = models.CharField(max_length=100)
    created_by=models.ForeignKey(MyUser,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name

    def to_json(self):
        return{
            'name': self.name,
            'id': self.id,
        }

class TaskManager(models.Manager):
    def for_user(self,user,pk):
        return self.filter(created_by=user).filter(task_list=pk)

class Task(models.Model):
    objects = TaskManager()
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    due_on = models.DateTimeField(default=datetime.now,blank=True)
    status = models.CharField(max_length=50,default="in process")
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE,related_name="tasks")
    created_by = models.ForeignKey(MyUser,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return '{}: {}'.format(self.due_on,self.name)

    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
            'created_by':self.created_by
        }

