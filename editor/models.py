from django.db.models import (
    # Fields
    BigAutoField,
    CharField,
    DateTimeField,
    ForeignKey,
    ImageField,
    ManyToManyField,

    # BaseModels
    Model,

    # Actions
    CASCADE,
    PROTECT,
)
from django.contrib.postgres.fields import JSONField


class Author(Model):
    """
    Author stores simple identity info about user
    """
    nick_name = CharField(max_length=40, unique=True, db_index=True)


class Drawing(Model):
    """
    Drawing describes all drawled objects
    stores drawing in mol1000 fmt
    and contain links to author, previous image (if exists) and preview
    """
    # service fields
    creation_date = DateTimeField(auto_created=True, auto_now_add=True)
    last_update = DateTimeField(auto_created=True, auto_now_add=True)

    # user related fields
    author = ForeignKey('Author', on_delete=PROTECT)

    # picture related fields
    title = CharField(max_length=80)
    description = CharField(max_length=1200)
    data = JSONField(default=dict)


class Comment(Model):
    time = DateTimeField(auto_created=True, auto_now_add=True)
    drawing = ForeignKey('Drawing', on_delete=CASCADE)
    comment = CharField(max_length=240)
