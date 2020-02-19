from django.contrib import admin
from django.db import models
from main.models import Todo
from user.models import MyUser


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed')


