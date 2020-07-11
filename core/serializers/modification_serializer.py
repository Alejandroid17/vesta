from rest_framework.serializers import BaseSerializer


class ModificationSerializer(BaseSerializer):
    # modified_by = UserSerializer()

    class Meta:
        fields = ['modified_at']
