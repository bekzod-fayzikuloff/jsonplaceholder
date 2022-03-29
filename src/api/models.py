from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model declaring
    with:
        ~`title`
        ~`body`
        ~`user`
    fields
    """

    title = models.CharField(max_length=255)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return f"{self.user.username}<->{self.title}"


class Comment(models.Model):
    """
    Comment model declaring
    with:
        ~`name`
        ~`email`
        ~`body`
    fields
    """

    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.CharField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return f"{self.email}"


class Album(models.Model):
    """
    Album model declaring
    with:
        ~`user`
        ~`title`
    fields
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self) -> str:
        return f"{self.user.username}<->{self.title}"


class Photo(models.Model):
    """
    Photo model declaring
    with:
        ~`album`
        ~`title`
    fields
    """

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"

    def __str__(self) -> str:
        return f"{self.title}"


class Todo(models.Model):
    """
    Todo model declaring
    with:
        ~`user`
        ~`title`
        ~`completed`
    fields
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self) -> str:
        return f"{self.title}"
