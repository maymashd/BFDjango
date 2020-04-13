from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token

from _auth.views import login,logout
urlpatterns = [
    path('login', obtain_jwt_token),

]
