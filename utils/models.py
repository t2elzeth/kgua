from django.db import models
from rest_framework import serializers


class MultilanguageModel(models.Model):
    repr_key: str = NotImplemented

    def __str__(self):
        return f"{self._get_repr_field(self.ru)} | {self._get_repr_field(self.kg)} | {self._get_repr_field(self.en)}"

    def _get_repr_field(self, field):
        return getattr(field, self.repr_key)

    class Meta:
        abstract = True


class AbstractModelWithGenericSerializer(models.Model):
    fields: list[str] = NotImplemented

    @classmethod
    def get_serializer(cls):
        class GenericSerializer(serializers.ModelSerializer):
            class Meta:
                model = cls
                fields = cls.fields
                ref_name = cls.__class__.__name__

        return GenericSerializer(read_only=True)

    class Meta:
        abstract = True
