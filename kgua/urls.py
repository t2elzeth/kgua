from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="KGUA Backend",
        default_version="v1",
        description="This is backend for KGUA",
        contact=openapi.Contact(url="https://telegram.me/t2elzeth"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("api/v1/auth/", include("authorization.urls")),
    path("api/v1/news/", include("news.urls")),
    path("api/v1/", include("staff.urls")),
    path("api/v1/documents/", include("documents.urls")),
    path("api/v1/life/", include("kgua_life.urls")),
    path(
        "api/v1/international_cooperation/",
        include("international_cooperation.urls"),
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
