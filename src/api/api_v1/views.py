from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ..models import Post, Comment, Album, Photo, Todo
from .serializers import (
    PostSerializer,
    CommentSerializer,
    AlbumSerializer,
    PhotoSerializer,
    TodoSerializer,
    UserSerializer,
)


class PostViewSet(ModelViewSet):
    """
    PostViewSet define posts endpoints handlers
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=["GET"], detail=True, url_path=r"comments")
    def get_comments(self, _, pk):
        comments = Comment.objects.filter(post_id=pk)
        data = CommentSerializer(comments, many=True).data
        return Response(data)


class CommentViewSet(ModelViewSet):
    """
    CommentViewSet define comments endpoints handlers
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        post_id = self.request.GET.get("postID")
        if post_id:
            post_comments = self.queryset.filter(post_id=post_id)
            data = CommentSerializer(post_comments, many=True).data
            return Response(data)

        return super().list(request, *args, **kwargs)


class AlbumViewSet(ModelViewSet):
    """
    AlbumViewSet define albums endpoints handlers
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PhotoViewSet(ModelViewSet):
    """
    PhotoViewSet define photos endpoints handlers
    """

    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class TodoViewSet(ModelViewSet):
    """
    TodoViewSet define todos endpoints handlers
    """

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class UserViewSet(ModelViewSet):
    """
    UserViewSet define users endpoints handlers
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
