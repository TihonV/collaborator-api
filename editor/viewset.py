from rest_framework.viewsets import (
    ModelViewSet,
    ReadOnlyModelViewSet,
)

from . import serializers
from .models import Drawing, Author


class AuthorViewset(ModelViewSet):
    serializer_class = serializers.AuthorSerializer
    queryset = serializer_class.Meta.queryset

    http_method_names = ('get', 'post', 'options')


class UserViewset(AuthorViewset):
    lookup_field = 'nick_name'


class ViewDrawingViewset(ModelViewSet):
    queryset = serializers.DrawingSerializer.Meta.queryset
    serializer_class = serializers.DrawingSerializer

