from rest_framework.viewsets import (
    ModelViewSet,
    ReadOnlyModelViewSet,
)
from django_filters.rest_framework import DjangoFilterBackend

from . import serializers
from .models import Drawing, Author


class AuthorViewset(ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = serializer_class.Meta.queryset

    http_method_names = ('get', 'post', 'options')


class UserViewset(AuthorViewset):
    lookup_field = 'nick_name'


class CommentViewset(ModelViewSet):
    queryset = serializers.CommentSerializer.Meta.queryset
    serializer_class = serializers.CommentSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('drawing', )


class ViewDrawingViewset(ModelViewSet):
    queryset = serializers.DrawingSerializer.Meta.queryset
    serializer_class = serializers.DrawingSerializer

