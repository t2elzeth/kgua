from django.contrib import admin

from .models import InternationalEvent, InternationalProgram, PartnerOrganization

admin.site.register(InternationalEvent)
admin.site.register(InternationalProgram)
admin.site.register(PartnerOrganization)
