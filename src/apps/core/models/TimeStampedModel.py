from django.db.models import DateTimeField
from django.db.models import Model

class TimeStampedModel(Model):
    created = DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modified = DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True        