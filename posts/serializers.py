from rest_framework import serializers

from .models import Post, Comment, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'username',)
        model = User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment