from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers

from core.serializers import (UUIDSerializer, ModificationSerializer, CreationSerializer)
from group.serializers import GroupSerializer
from user.models import User


class UserSerializer(DynamicFieldsMixin, serializers.HyperlinkedModelSerializer, UUIDSerializer,
                     ModificationSerializer, CreationSerializer):
    groups = GroupSerializer(many=True)

    class Meta(UUIDSerializer.Meta, ModificationSerializer.Meta, CreationSerializer.Meta):
        model = User
        fields = UUIDSerializer.Meta.fields + ModificationSerializer.Meta.fields + CreationSerializer.Meta.fields + [
            'email', 'first_name', 'last_name', 'groups']
