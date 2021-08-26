from django.contrib import admin

from . import models

admin.site.register(models.Event)
admin.site.register(models.Promotion)
admin.site.register(models.Charity)
admin.site.register(models.Jubilee)
admin.site.register(models.Mug)
