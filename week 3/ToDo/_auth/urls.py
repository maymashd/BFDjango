from django.contrib import admin
from django.urls import path,include
from _auth.views import login,logout
urlpatterns = [
    path('login', login ),
    path('logout',logout),


]
