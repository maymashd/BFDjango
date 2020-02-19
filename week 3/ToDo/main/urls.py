from django.urls import path
from main.views import TodoListAPiView, TodoDetailAPIView

urlpatterns = [

    path('todo_list/', TodoListAPiView.as_view()),
    path('todo_list/<int:pk>/', TodoDetailAPIView.as_view()),
]