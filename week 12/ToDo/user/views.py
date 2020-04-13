from rest_framework import mixins,viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView,Response
from user.models import MyUser
from user.serializers import MyUserSerializer, MyUserShortSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission, AllowAny


class MyOnwPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        print(view)
        return True

class UserLists(    mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin):

    queryset = MyUser.objects.all()

    def get_serializer_class(self):
        if self.action=='list':
            return MyUserShortSerializer
        else:
            return MyUserSerializer

    def get_permissions(self):
        if self.action=='destroy':
            permission_classes=[AllowAny,]
            print("ok")
        else:
            permission_classes=[IsAdminUser,]
        return (permission() for permission in permission_classes)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        if (request.user==instance):
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


