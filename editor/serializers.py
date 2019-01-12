from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from .models import Author, Tag, Drawing


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        queryset = model.objects.all()
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        queryset = model.objects.all()
        fields = ('name', )


class DrawingListSerializer(ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    tag_keys = PrimaryKeyRelatedField(source='tags')

    class Meta:
        model = Drawing
        queryset = model.objects.annotate().all()
        fields = (
            'id', 'author', 'title', 'tags', 'tag_keys'
            'preview', 'next',
            # 'comment_count',  # TODO: Must be implemented
        )


class DrawingWriteSerializer(DrawingListSerializer):
    class Meta(DrawingListSerializer.Meta):
        fields = (
            'id', 'author', 'last_update',
            'tags', 'title',  'date',
            # Stores JSON with mol1000-content
            'data',
        )


class DrawingReadSerializer(DrawingListSerializer):
    class Meta(DrawingListSerializer.Meta):
        read_only_fields = (
            'id', 'author', 'creation_date', 'date',
            'last_update', 'tags', 'title', 'previous'
        )
