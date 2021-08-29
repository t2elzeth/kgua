from rest_framework import serializers
from django.conf import settings


class MultilanguageField(serializers.Field):
    def __init__(self, lang: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang

    def get_attribute(self, instance):
        return instance

    def to_representation(self, obj):
        translated_fields = [
            el
            for el in obj.__dict__.keys()
            if not el.startswith("__")
            and not el.endswith("__")
            and el.endswith(self.lang)
        ]
        res = {}
        for f in translated_fields:
            key = f.rsplit("_", 1)[0]
            res[key] = getattr(obj, f)

        return res


class MultilanguageModelSerializer(serializers.ModelSerializer):
    def get_field_names(self, declared_fields, info):
        return super().get_field_names([*declared_fields], info)

    @property
    def data(self):
        data = super().data

        languages = list(map(lambda el: el[0], settings.LANGUAGES))
        query_lang = self.context['request'].query_params.get('lang')
        if query_lang not in languages:
            query_lang = "ru"

        translated_fields = [
            el
            for el in self.instance.__dict__.keys()
            if el.endswith(query_lang)
        ]
        res = {}
        for f in translated_fields:
            key = f.rsplit("_", 1)[0]
            res[key] = getattr(self.instance, f)

        print(res)
        data.update(res)
        return data
