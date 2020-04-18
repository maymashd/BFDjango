from django.urls import path

from main.views_viewset import GroupListView, UserRegister
from .views import GroupLists,GroupListDetail,Tasks,TaskDetail
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'task_list', GroupListView)
router.register(r'register', UserRegister)

urlpatterns = [
    # path('task_list/', GroupLists.as_view() ),
    # path('^',include(router.urls)),
    # path('task_list/<int:pk>/', GroupListDetail.as_view()),
    path('task_list/<int:pk>/tasks/',Tasks.as_view()),
    path('task_list/<int:pk2>/tasks/<int:pk>/',TaskDetail.as_view()),

]

urlpatterns =urlpatterns + router.urls