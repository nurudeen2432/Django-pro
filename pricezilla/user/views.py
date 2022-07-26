from django import views
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
import requests

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def home(request):
    response = requests.get('http://127.0.0.1:8000/user/')
    data = response.json()
    return HttpResponse(response)