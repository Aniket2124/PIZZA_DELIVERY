from django.shortcuts import render
from .serializers import UserCreationSerializer
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserCreateview(CreateAPIView):

    serializer_class = UserCreationSerializer

    def post(self, request):
        data = request.data

        serializer  = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

