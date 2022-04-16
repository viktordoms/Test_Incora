from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserProfileSerializer
from .models import User


class UserCreate(APIView):

    # Потім видалити
    def get(self, request, format=None):
        snippets = User.objects.all()
        serializer = UserProfileSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            exist_email = User.objects.filter(email=request.data['email'])
            if exist_email:
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
            exist_email = User.objects.filter(email=request.data['email']).exclude(id=pk)
            if exist_email:
                return Response('User with this email is already exist', status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
