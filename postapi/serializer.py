from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author']


class UserPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        posts_data = PostSerializer(instance.post_set.all(), many=True).data
        representation['posts'] = posts_data
        return representation


