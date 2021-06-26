from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ("is_staff",)

    list_display = ("username", "is_staff")

    list_filter = ("is_staff",)

    readonly_fields = ("id",)
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
                    "user_permissions",
                    "groups",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(models.User, UserAdmin)
