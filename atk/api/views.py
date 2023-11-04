from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .serializer import ForumPostSerializer
from .models import ForumPost
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# View list of forum posts
class ForumPostListView(generics.ListAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer