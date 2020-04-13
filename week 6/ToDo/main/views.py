from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import TaskList, Task
from main.serializers import ListSerializer, ListSerializer2, TaskSerializer


class GroupLists(mixins.ListModelMixin,
                 generics.GenericAPIView,
                 mixins.CreateModelMixin):
    serializer_class = ListSerializer2
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def get(self, request, *args, **kwargs):
        # self.queryset = self.get_queryset().filter(created_by=request.user)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GroupListDetail(generics.GenericAPIView,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ListSerializer2

    def get_queryset(self):
        return TaskList.objects.for_user(self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class Tasks(mixins.ListModelMixin,
            generics.GenericAPIView,
            mixins.CreateModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user(self.request.user, self.kwargs.get('pk', 1))

    def get(self, request, *args, **kwargs):
        #  self.queryset=self.get_queryset().filter(created_by=request.user).filter(task_list=kwargs.get('pk',1))
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaskDetail(mixins.RetrieveModelMixin,
                 generics.GenericAPIView,
                 mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin):
    queryset = TaskList.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     return Task.objects.for_user(self.request.user,self.kwargs.get('pk2',1))

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
