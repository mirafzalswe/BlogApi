from rest_framework import generics, status
from django.contrib.auth.models import User

from .models import Post
from .serializer import PostSerializer, UserPostsSerializer

class PostApiCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostsAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostsSerializer
    lookup_field = 'username'

class PostUpdateRetriveDelteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer





