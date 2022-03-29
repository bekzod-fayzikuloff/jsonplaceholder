from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet, AlbumViewSet, PhotoViewSet, TodoViewSet, UserViewSet

router = SimpleRouter()

router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"albums", AlbumViewSet)
router.register(r"photos", PhotoViewSet)
router.register(r"todos", TodoViewSet)
router.register(r"users", UserViewSet)
