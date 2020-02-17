from django.http import Http404
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView,Response
from user.models import MyUser
from user.Serializers import MyUserSerializer
from rest_framework.permissions import IsAuthenticated
class UserLists(APIView):
    permission_classes = {IsAuthenticated}
    def get(self, request):
        lists = MyUser.objects.all()
        serializer = MyUserSerializer(lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
