from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CharField,
)
from django.db.models import F
from .models import Author, Drawing, Comment


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        queryset = model.objects.all()
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        queryset = model.objects.all()
        fields = '__all__'


class DrawingSerializer(ModelSerializer):
    """
    Limited queryset to active user (described in related Viewset)
    """

    author = PrimaryKeyRelatedField(queryset=AuthorSerializer.Meta.queryset)
    author_name = CharField(read_only=True, source='author__nick_name')

    class Meta:
        model = Drawing
        queryset = model.objects\
            .select_related('author')\
            .prefetch_related('comment_set')\
            .all()
        fields = '__all__'
