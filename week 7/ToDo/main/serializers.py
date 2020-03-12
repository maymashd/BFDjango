from rest_framework import serializers
from .models import Task, TaskList
import user.serializers


class ListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        li = TaskList(**validated_data)
        li.save()
        return li

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ListSerializer2(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name',)


class ListFullSerializer2(ListSerializer2):
    created_by = user.serializers.MyUserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by', )



class TaskShortSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model=Task
        fields=('id', 'name', 'status',)

class TaskSerializer(TaskShortSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    due_on = serializers.DateTimeField(read_only=True)
    created_by = user.serializers.MyUserSerializer(default=serializers.CurrentUserDefault())
    task_list_id = serializers.IntegerField(write_only=True)

    #
    # created_by_id = serializers.HiddenField()

    class Meta:
        model = Task
        fields = TaskShortSerializer.Meta.fields + ( 'created_at', 'due_on', 'created_by', 'task_list_id',)

    def validate_task_list_id(self, val):
        if val<=0:
            raise serializers.ValidationError('task list id can not be 0 or negative!!!')
        return val
