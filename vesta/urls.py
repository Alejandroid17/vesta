from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from core.api.schemas.schema_view import schema_view
from user.api import UserModelViewSet

router = DefaultRouter()
router.register(r'user', UserModelViewSet, basename='user')

urlpatterns = [
    # API documentation and playground
    path(r'^api-doc/$', schema_view.with_ui('redoc', cache_timeout=0), name='api-doc'),
    path(r'^api-playground(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
         name='api-playground-json'),
    path(r'^api-playground/$', schema_view.with_ui('swagger', cache_timeout=0), name='api-playground-ui'),

    # Admin
    path(r'admin/', admin.site.urls),

    # Authentication token
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # API
    path(r'', include(router.urls))
]

urlpatterns += staticfiles_urlpatterns()
