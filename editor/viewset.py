from rest_framework.viewsets import (
    ModelViewSet,
    ReadOnlyModelViewSet,
)

from . import serializers
from .models import Tag, Drawing, Author


class AuthorViewset(ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = serializer_class.Meta.queryset


class TagViewset(ReadOnlyModelViewSet):
    serializer_class = serializers.TagSerializer
    queryset = serializer_class.Meta.queryset


class ViewDrawingViewset(ReadOnlyModelViewSet):
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.DrawingListSerializer
        return serializers.DrawingReadSerializer

    def get_queryset(self):
        return self.get_serializer_class().Meta.queryset


class EditDrawingViewset(ModelViewSet):
    serializer_class = serializers.DrawingWriteSerializer
    queryset = serializer_class.Meta.queryset
