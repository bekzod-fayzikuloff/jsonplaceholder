"""placeholder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.api_v1.urls import router as api_router

schema_view = get_schema_view(
    openapi.Info(
        title=settings.DOCS_API_TITLE,
        default_version=settings.DOCS_API_VERSION,
        description=settings.DOCS_API_DESCRIPTION,
        terms_of_service=settings.DOCS_TERM_OF_SERVICE,
        contact=openapi.Contact(email=settings.DOCS_CONTACT_EMAIL),
        license=openapi.License(name=settings.DOCS_API_LICENSE),
    ),
    public=settings.DOCS_IS_PUBLIC,
    permission_classes=(permissions.AllowAny,),
)

v1_router = DefaultRouter()
v1_router.registry.extend(api_router.registry)

urlpatterns = [
    path("api/v1/", include((v1_router.urls, "api"), namespace="v1")),
    path("admin/", admin.site.urls),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
