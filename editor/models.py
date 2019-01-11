from django.db.models import (
    BigAutoField,
    BooleanField,
    CharField,
    DateTimeField,
    Model,
)
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Tags(Model):
    id = BigAutoField(primary_key=True)
    name = CharField(primary_key=True)


class Drawing(Model):
    pass


class ApprovedDrawing(Drawing):
    pass


class History(Model):
    pass
