from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from ...models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['posts', 'id']


class TagDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['posts', 'id']

    posts_count = serializers.SerializerMethodField()

    # @extend_schema_field(serializers.IntegerField)
    def get_posts_count(self, instance) -> int:
        return instance.posts.count()
