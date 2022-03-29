from django.contrib import admin
from .models import Post, Comment, Album, Photo, Todo


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "user"]
    list_filter = ["title", "user"]
    search_fields = ["title", "user__username"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    list_filter = ["name", "email"]
    search_fields = ["name", "email"]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["user", "title"]
    search_fields = ["user__username", "title"]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["album", "title"]
    search_fields = ["album__title", "title", "album__user__username"]


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ["user", "title"]
    search_fields = ["user__username", "title"]
