from django.urls import path

from .views import PostListAPIView, PostDetailAPIView, TagListAPIView, VolunteerListAPIView

urlpatterns = [
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>', PostDetailAPIView.as_view(), name='post-detail'),
    path('volunteers/', VolunteerListAPIView.as_view(), name='volunteers')
]
