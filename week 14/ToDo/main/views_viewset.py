from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from rest_framework import mixins
from django.db.models import Count
from rest_framework.response import Response

from main.models import TaskList
from main.serializers import ListSerializer2
from user.models import MyUser
from user.serializers import MyUserSerializer
import logging
logger=logging.getLogger(__name__)

class GroupListView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    def filter_queryset(self, queryset):
        return TaskList.objects.for_user(self.request.user)

    permission_classes = [IsAuthenticated, ]
    queryset = TaskList.objects.all()
    serializer_class = ListSerializer2

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'New group is created :{serializer.instance}')


    @action(methods=['GET'],detail=False)
    def reverse(self,request):
        self.queryset=TaskList.objects.all().order_by('-id')
        return self.list(request)

class UserRegister(mixins.CreateModelMixin,viewsets.GenericViewSet):

    queryset = MyUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = MyUserSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'New user is created :{serializer.instance}')




