from rest_framework import serializers
from django.conf import settings
from .models import Post, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_username', 'content', 'created_at']
        read_only_fields = ['author', 'created_at']


class LikeSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='author.username', read_only=True)
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'user_username', 'created_at']
        read_only_fields = ['user', 'created_at']


class PostSerializer(serializers.ModelSerializer):

    comments = serializers.SerializerMethodField(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    author_username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'author', 'author_username', 'content', 'image',
            'created_at','updated_at', 'comments', 'likes_count',
        ]
        read_only_fields = ['author', 'created_at', 'updated_at']

    def get_likes_count(self, obj):
        return obj.likes.count()