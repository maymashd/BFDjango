from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins
from main.models import Todo
from main.serializers import TodoSerializer


class TodoListAPiView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer