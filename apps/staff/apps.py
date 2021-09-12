from django.apps import AppConfig
from importlib import import_module


class StaffConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "staff"
    verbose_name = 'Преподаватели'

    def ready(self):
        import_module(".signals", "staff")
        return super().ready()
