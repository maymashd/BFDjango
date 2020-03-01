from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from .models import Task, TaskList
from user.models import MyUser


#@admin.register(TaskList)
#class TodoAdmin(UserAdmin):
 #   list_display = ('id', 'name', 'completed',)


#@admin.register(Task)
#class TodoAdmin(UserAdmin):
#   list_display = ('id', 'name', 'created_at', 'status','task_list','created_by')
admin.site.register(Task)
admin.site.register(TaskList)