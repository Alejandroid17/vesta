from rest_framework.serializers import BaseSerializer


class CreationSerializer(BaseSerializer):
    class Meta:
        fields = ['created_at']
