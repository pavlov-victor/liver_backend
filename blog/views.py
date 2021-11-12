from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
import django_filters.rest_framework

from blog.models import Post, PostTag
from blog.serializers import TagSerializer, PostSerializer


class TagListAPIView(ListAPIView):
    pagination_class = None
    serializer_class = TagSerializer
    queryset = PostTag.objects.all()


class PostListAPIView(ListAPIView):
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    queryset = Post.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['tags']
    search_fields = ['title']


class PostDetailAPIView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
