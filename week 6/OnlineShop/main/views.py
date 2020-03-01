from django.http import Http404
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView,Response
from main.models import MyUser, Category, Product, Order
from main.serializers import MyUserSerializer, MyCategorySerializer, MyProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins
class UserLists(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        if request.user.is_staff:
            lists = MyUser.objects.all()
            serializer = MyUserSerializer(lists, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserDetail(APIView):
    def get_user(self, pk):
        try:
            user=MyUser.objects.get(id=pk)
            return Response(user.to_json(), status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            raise Http404



class CategoryView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin):

    permission_classes = [IsAuthenticated, ]
    queryset = Category.objects.all()
    serializer_class = MyCategorySerializer


class ProductView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin):

    permission_classes = [IsAuthenticated, ]
    queryset = Product.objects.all()
    serializer_class = MyProductSerializer


class OrderView(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):

    permission_classes = [IsAuthenticated, ]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

