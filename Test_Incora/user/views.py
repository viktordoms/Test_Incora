from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserProfileSerializer
from .models import User


class UserCreate(APIView):

    def post(self, request, format='json'):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
            except:
                return Response('User with this email is already exist', status=status.HTTP_400_BAD_REQUEST)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        if user:
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        else:
            return Response('Not found', status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            try:
                 serializer.save()
            except:
                return Response('User with this email is already exist', status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
