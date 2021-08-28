from rest_framework import serializers
from django.conf import settings


class MultilanguageField(serializers.Field):
    def __init__(self, lang: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang

    def get_attribute(self, instance):
        return instance

    def to_representation(self, obj):
        translated_fields = [el for el in obj.__dict__.keys() if
                             not el.startswith("__") and not el.endswith("__") and el.endswith(self.lang)]
        res = {}
        for f in translated_fields:
            key = f.rsplit("_", 1)[0]
            res[key] = getattr(obj, f)

        return res


class MultilanguageModelSerializer(serializers.ModelSerializer):
    def get_field_names(self, declared_fields, info):
        return super().get_field_names([*declared_fields], info)

    def get_fields(self):
        res = super().get_fields()
        for lang in list(map(lambda el: el[0], settings.LANGUAGES)):
            res.update({lang: MultilanguageField(lang=lang, read_only=True)})
        return res