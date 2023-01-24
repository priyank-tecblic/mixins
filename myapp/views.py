from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserView(generics.GenericAPIView,mixins.ListModelMixin,mixins.DestroyModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request,*args,**kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)