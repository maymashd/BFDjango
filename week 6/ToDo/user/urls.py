from django.contrib import admin
from django.urls import path,include
from user.views import UserLists,UserDetail
urlpatterns = [
    path('<int:pk>/',UserDetail.as_view()),
    path('', UserLists.as_view()),


]
