from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Vesta API",
        default_version='v1',
        description="Test description",
        terms_of_service="",
        contact=openapi.Contact(email="vesta@support.com"),
        license=openapi.License(name="Joke License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


