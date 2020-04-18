from user.models import MyUser, MyUserProfile
from rest_framework import serializers

class MyUserShortSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email','logo',)

class MyUserSerializer(MyUserShortSerializer):

    class Meta:
        model = MyUser
        fields = MyUserShortSerializer.Meta.fields + ('password','first_name','last_name',)

    def create(self, validated_data):
        user = MyUser.objects.create_user(username=validated_data['username'],
                                          first_name=validated_data.get('first_name', ''),
                                          last_name=validated_data.get('last_name', ''),
                                          logo=validated_data.get('logo')
                                          )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self,val):
        fname=""
        fname=val.get('first_name')
        if len(fname)!=0:
            if fname[0]<'A' or fname[0]>'Z':
                raise serializers.ValidationError('The firstname of user can not start with Lower Case!!!')
        lname=""
        lname=val.get('last_name')
        if len(lname) != 0:
            if lname[0] < 'A' or lname[0] > 'Z':
                raise serializers.ValidationError('The lastname of user can not start with Lower Case!!!')
        return val

# class ProfileSerializer(serializers.ModelSerializer):
#
#     user=serializers.CurrentUserDefault()
#     class Meta:
#         model = MyUserProfile
#         fields = MyUserShortSerializer.Meta.fields + ('user', 'mobile', 'location','birth_date',)
