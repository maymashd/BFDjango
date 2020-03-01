from user.models import MyUser
from rest_framework import serializers


class MyUserSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email','mobile','location','birth_date',)