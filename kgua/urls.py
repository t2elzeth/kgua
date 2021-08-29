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
    # path("api/v1/auth/", include("authorization.urls")),

    # Новости
    path("api/v1/news/", include("news.urls")),

    # Вакансии
    path("api/v1/vacancies/", include("vacancies.urls")),

    # Преподаватели
    path("api/v1/staff/", include("staff.urls")),

    # Кафедры
    path("api/v1/department/", include("department.urls")),

    # Клубы
    path("api/v1/clubs/", include("clubs.urls")),

    # Мероприятия
    path("api/v1/events/", include("event.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
