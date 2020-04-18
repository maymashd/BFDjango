from django.contrib import admin
from django.urls import path,include
from main.views import UserDetail, UserLists, CategoryView, ProductView, OrderView, UserRegister, UserNotifications
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'category',CategoryView)
router.register(r'product',ProductView)
router.register(r'order',OrderView)
router.register(r'users',UserLists)
router.register(r'register',UserRegister)
router.register(r'notifications',UserNotifications,base_name="notifications")
urlpatterns = router.urls
