from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins

from core.api.parameters import query_parameter
from core.viewsets import BaseModelViewSet
from user.models import User
from user.serializers import UserSerializer


@method_decorator(name='retrieve', decorator=swagger_auto_schema(manual_parameters=[query_parameter]))
class UserModelViewSet(mixins.RetrieveModelMixin,
                       BaseModelViewSet):
    lookup_field = 'email'
    lookup_value_regex = r'[\w.@+-]+'

    action_serializers = {
        'retrieve': UserSerializer
    }

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
