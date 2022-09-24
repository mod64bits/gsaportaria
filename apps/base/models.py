from django.db import models
import uuid

from safedelete.models import SafeDeleteModel

from safedelete.models import SOFT_DELETE


class BaseModelSlug(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    slug_field_name = 'slug'
    #slug_from = 'nome'

    class Meta:
        abstract = True


class BaseModelUUID(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(
        'Cadastrado em', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        'Modificado em', auto_now=True, null=True)

    class Meta:
        abstract = True
