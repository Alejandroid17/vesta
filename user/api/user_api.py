from rest_framework import mixins

from core.viewsets import BaseModelViewSet
from user.serializers import UserSerializer
from user.models import User


class UserModelViewSet(mixins.RetrieveModelMixin,
                       BaseModelViewSet):
    lookup_field = 'email'
    lookup_value_regex = r'[\w.@+-]+'

    action_serializers = {
        'retrieve': UserSerializer
    }

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
