from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', views.feed_view, name='feed'),
    path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike-post'),
]
