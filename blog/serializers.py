from rest_framework import serializers

from blog.models import Post, PostTag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = '__all__'


class PostRelativeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['title', 'id', 'description', 'tags']

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    foreign_posts = serializers.SerializerMethodField()

    def get_foreign_posts(self, obj: Post):
        return PostRelativeSerializer([x.foreign for x in obj.foreign_posts.all()], many=True).data

    class Meta:
        model = Post
        fields = '__all__'
