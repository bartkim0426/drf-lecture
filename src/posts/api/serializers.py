from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # "user",
            # "id",
            "title",
            "content",
            # "slug",
            "publish",
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "user",
            "id",
            "title",
            "content",
            "slug",
            "publish",
        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "user",
            "id",
            "title",
            "content",
            "slug",
            "publish",
        ]
"""
data = {
    "title": "new_title_2",
    "content": "content2",
    "slug": "slug2",
    "publish": "2017-2-12",
}

obj = Post.obejcts.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""
