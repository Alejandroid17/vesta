from django.contrib.auth.models import Group
from django_restql.mixins import DynamicFieldsMixin
from rest_framework import serializers


class GroupSerializer(DynamicFieldsMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['uuid', 'name', 'label']
