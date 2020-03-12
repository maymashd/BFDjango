from django.http import Http404
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView,Response
from main.models import MyUser, Category, Product, Order
from main.serializers import MyUserSerializer, MyCategorySerializer, MyProductSerializer, OrderSerializer, \
    MyUserShortSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins
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




class UserDetail(APIView):
    def get_user(self, pk):
        try:
            user=MyUser.objects.get(id=pk)
            return Response(user.to_json(), status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            raise Http404



class CategoryView( mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    queryset = Category.objects.all()
    serializer_class = MyCategorySerializer
    def get_permissions(self):
        if self.action=='list' or self.action=='retrieve':
            permission_classes=[AllowAny]
        else:
            permission_classes= [IsAdminUser]
        return (permission() for permission in permission_classes)

class ProductView( mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    queryset = Product.objects.all()
    serializer_class = MyProductSerializer
    def get_permissions(self):
        if self.action=='list' or self.action=='retrieve':
            permission_classes=[AllowAny]
        else:
            permission_classes= [IsAdminUser]
        return (permission() for permission in permission_classes)


class OrderView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    permission_classes = [IsAuthenticated, ]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class UserRegister(mixins.CreateModelMixin,viewsets.GenericViewSet):

    queryset = MyUser.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = MyUserSerializer


