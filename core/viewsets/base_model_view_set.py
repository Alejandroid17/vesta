from rest_framework import viewsets


class BaseModelViewSet(viewsets.GenericViewSet):
    action_serializers = None

    def get_serializer_class(self, *args, **kwargs):
        """Overrides `get_serializer_class` method to get the corresponding method depending on the request method.
        """
        assert self.action_serializers is not None, (
            '"{}" should either include a `action_serializers` attribute'.format(self.__class__.__name__))
        if hasattr(self, 'action'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
            else:
                raise ValueError('There is no serializer defined for the action {action}'.format(action=self.action))

    def get_permissions(self):
        """Overrides `get_permissions` method to get the corresponding permissions depending on the request action.
        """
        if hasattr(self, 'action'):
            if self.action in self.permission_classes:
                return [permission() for permission in self.permission_classes[self.action]]
            return [permission() for permission in self.permission_classes]
