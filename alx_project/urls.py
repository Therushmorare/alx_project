# alx_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from listings.views import api_overview  # import your function-based view

# Swagger/OpenAPI schema view
schema_view = get_schema_view(
    openapi.Info(
        title="ALX Project API",
        default_version='v1',
        description="API documentation for ALX Project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),  # make sure this exists
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', api_overview, name='api-overview'),  # root URL now shows API overview
]
