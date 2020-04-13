from django.contrib import admin
from django.urls import path,include
from main.views import UserDetail, UserLists, CategoryView, ProductView, OrderView, UserRegister
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'category',CategoryView)
router.register(r'product',ProductView)
router.register(r'order',OrderView)
router.register(r'users',UserLists)
router.register(r'register',UserRegister)
urlpatterns = router.urls
