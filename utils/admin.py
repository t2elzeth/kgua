from modeltranslation.admin import TranslationAdmin
from django.conf import settings


def is_multilang(field_name):
    for lang in settings.LANGUAGES_LIST:
        if lang in field_name:
            return True

    return False


class MultilanguageModelAdmin(TranslationAdmin):
    def get_fieldsets(self, request, obj=None):
        fields = super().get_fieldsets(request, obj)[0][1]['fields']

        multilang_fields = [field for field in fields if is_multilang(field)]
        other_fields = list(set(fields) - set(multilang_fields))

        fieldsets_dict = {None: {'fields': other_fields}}

        for lang in settings.LANGUAGES_LIST:
            singlelang_fields = [field for field in multilang_fields if lang in field]
            fieldsets_dict.update({
                settings.LANGUAGE_NAME[lang]: {
                    'fields': singlelang_fields
                }
            })
        return fieldsets_dict.items()
