from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from ddev.models import *
from ddev.serializers import *

class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (IsAuthenticated)

class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated)

class ResultViewSet(viewsets.ModelViewSet):
    
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (IsAuthenticated)
