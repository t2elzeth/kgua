from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ("is_staff",)

    list_display = ("username",)

    list_filter = ("is_staff",)

    readonly_fields = ("id", "is_superuser", "is_staff")
    add_fieldsets = (
        (
            "Authentication data",
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )

    fieldsets = (
        (
            "User data",
            {
                "fields": (
                    "id",
                    "email",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                )
            },
        ),
    )


admin.site.register(models.User, UserAdmin)

admin.site.unregister(Group)
