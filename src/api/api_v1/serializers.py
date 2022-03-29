import random

from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Post, Comment, Album, Photo, Todo


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "body", "user"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["name", "email", "body", "post"]
        depth = 1


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ["user", "title"]


class PhotoSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    def get_url(self, obj):  # noqa
        return random.choice(["https://placebeard.it/640/480", "https://placebeard.it/g/640/480"])

    def get_thumbnail_url(self, obj):  # noqa
        return random.choice(["https://placebeard.it/150/150", "https://placebeard.it/g/150/150"])

    class Meta:
        model = Photo
        fields = ["album", "title", "url", "thumbnail_url"]


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["user", "title", "completed"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
