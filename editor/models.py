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
    SET_NULL,
    CASCADE,
)
from django.contrib.postgres.fields import JSONField


class Author(Model):
    """
    Author stores simple identity info about user
    """
    nick_name = CharField(max_length=40, unique=True, db_index=True)
    full_name = CharField(max_length=240, unique=False)


class Tag(Model):
    """
    Tag may help on search actioins
    """
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=24, unique=True)


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
    author = ForeignKey('Author', on_delete=SET_NULL)

    # picture related fields
    tags = ManyToManyField('Tag')
    title = CharField(max_length=120)
    date = JSONField(default={})

    parent = ForeignKey('self', on_delete=SET_NULL)
    preview = ImageField()

    def generate_preview(self):
        raise NotImplementedError("May be implemented in future stage")

    def export_drawing(self):
        raise NotImplementedError("Must be implemented in subclass.")

    def import_drawing(self):
        raise NotImplementedError("May be implemented in future stage")

    # TODO: Comment management
