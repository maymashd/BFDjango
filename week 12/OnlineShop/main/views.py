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
import logging
logger=logging.getLogger(__name__)
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
        name = request.data.get('id')
        logger.info(f'User has been deleted. id: {name}')
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

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'The new category was created: {serializer.data}')

    def perform_update(self, serializer):

        serializer.save()
        logger.info(f'The category was updated: {serializer.data}')


    def perform_destroy(self, instance):

        logger.info(f'The category was deleted: {instance}')
        instance.delete()

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

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'The new product was created: {serializer.data}')

    def perform_update(self, serializer):

        serializer.save()
        logger.info(f'The product was updated: {serializer.data}')


    def perform_destroy(self, instance):

        logger.info(f'The product was deleted: {instance}')
        instance.delete()


class OrderView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    permission_classes = [IsAuthenticated, ]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def perform_create(self, serializer):
        serializer.save()

        logger.info(f'New order has been created: {serializer.info}')

    def perform_update(self, serializer):
        serializer.save()
        logger.info(f'The order has been updated. {serializer.data}')

    def perform_destroy(self, instance):
        logger.info(f'The order has been updated. {instance}')
        instance.delete()



class UserRegister(mixins.CreateModelMixin,viewsets.GenericViewSet):

    queryset = MyUser.objects.all()
    permission_classes = [AllowAny,]
    serializer_class = MyUserSerializer

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f'New user has been created:{serializer.data}')



