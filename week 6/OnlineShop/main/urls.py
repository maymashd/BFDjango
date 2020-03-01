from django.contrib import admin
from django.urls import path,include
from main.views import UserDetail, UserLists, CategoryView, ProductView, OrderView
from rest_framework.routers import DefaultRouter
urlpatterns = [
    path('users/', UserLists.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

router=DefaultRouter()
router.register(r'category',CategoryView)
router.register(r'product',ProductView)
router.register(r'order',OrderView)


urlpatterns =urlpatterns + router.urls
