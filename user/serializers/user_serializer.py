from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from group.serializers import GroupSerializer
from user.models import User


class UserSerializer(DynamicFieldsMixin, serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['uuid', 'email', 'first_name', 'last_name', 'groups']
