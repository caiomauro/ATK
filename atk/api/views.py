from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializer import userInfoSerializer
from .models import userInfo
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

#view list of user

class userInfoView(generics.ListAPIView):
    queryset = userInfo.objects.all()
    serializer_class = userInfoSerializer



