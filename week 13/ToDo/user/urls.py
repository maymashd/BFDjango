from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from user.views import UserLists

router=DefaultRouter()
router.register(r'',UserLists)
urlpatterns = router.urls
