from datetime import datetime

from main.models import MyUser, Category, Order
from rest_framework import serializers


class MyUserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email','mobile','location','birth_date',)

class MyCategorySerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at =serializers.DateTimeField(default=datetime.now)
    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at',)


class MyProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(default=datetime.now)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at','category_id',)

class OrderSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    #status = models.CharField(max_length=50, default="in process")
    product_id=serializers.IntegerField(required=True)
    created_by=MyUserSerializer(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(default=datetime.now)
    class Meta:
        model=Order
        fields=('id','status','product_id','created_by','created_at','address',)

