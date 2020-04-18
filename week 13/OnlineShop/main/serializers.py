from datetime import datetime

from main.models import MyUser, Category, Order, Notification
from rest_framework import serializers


import logging
logger=logging.getLogger(__name__)
class MyUserShortSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email','photo',)

class MyUserSerializer(MyUserShortSerializer):

    class Meta:
        model = MyUser
        fields = MyUserShortSerializer.Meta.fields + ('mobile','location','birth_date','password','first_name','last_name',)

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'],
                                          first_name=validated_data.get('first_name', ''),
                                          last_name=validated_data.get('last_name', ''),
                                          birth_date=validated_data.get('birth_date', "1999-07-04"),
                                          mobile=validated_data.get('mobile',""),
                                          location=validated_data.get('location',""),
                                          photo=validated_data.get('photo'))
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self,val):
        fname=val.get('first_name')
        if len(fname)!=0:
            if fname[0]<'A' or fname[0]>'Z':
                logger.error(f'Incorrect firstname of user:{fname}')
                raise serializers.ValidationError('The firstname of user can not start with Lower Case!!!')
        lname=val.get('last_name')
        if len(lname) != 0:
            if lname[0] < 'A' or lname[0] > 'Z':
                logger.error(f'Incorrect last_name of user:{lname}')
                raise serializers.ValidationError('The lastname of user can not start with Lower Case!!!')
        return val

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
        fields = ('id', 'name', 'created_at', 'category_id',)

class OrderShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product_id = serializers.IntegerField(required=True)
    class Meta:
        model=Order
        fields=('id','status','product_id',)

class OrderFullSerializer(serializers.ModelSerializer):
    created_by=MyUserSerializer(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(default=datetime.now)
    class Meta:
        model=Order
        fields=OrderShortSerializer.Meta.fields+('created_by','created_at','address','quantity')

    def validate_quantity(self,val):

        if val<=0:
            logger.error(f'The quantity could not be negative!')
            raise serializers.ValidationError('The quantity could not be negative!!!!')


class NotificationSerializer(serializers.ModelSerializer):

    product=MyProductSerializer()
    class Meta:
        model=Notification
        fields=('product',)