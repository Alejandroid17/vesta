from rest_framework.serializers import BaseSerializer


class UUIDSerializer(BaseSerializer):
    class Meta:
        fields = ['uuid']
