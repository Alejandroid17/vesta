"""
Django rest framework siempre jwt settings.

See Also:
  - https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html
"""
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
