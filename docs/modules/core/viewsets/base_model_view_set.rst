Base model view set
===================

All model view set must inherit from ``BaseModelViewSet``. This class provides a generic way 
of defining serializers and permissions for each action.

How to use
----------

Define you model view set::

    class MyModelViewSet(BaseModelViewSet):

        lookup_field = 'email'
    
        ....

Define a ``dict`` called ``action_serializers`` where the keys is the action and the value 
will be the serializer that will be used::

    action_serializers = {
        'my_action': MySerializer
    }

Define a ``dict`` called ``permission_classes`` where the keys is the action and the value 
will be the permission class that will be used::

    permission_classes = {
        'my_action': MyPermissionClass
    }

Example
^^^^^^^

In this example we can see a ``MyModelViewSet`` model view set with a ``retrive`` and ``my_action`` endpoint::

    class MyModelViewSet(mixins.RetrieveModelMixin,
                        BaseModelViewSet):
        lookup_field = 'email'
        
        action_serializers = {
            'retrieve': UserSerializer
        }

        permission_classes = {
            'retrieve': (IsAuthenticated),
            'my_action': (IsAuthenticated)
        }

        def get_queryset(self):
            return User.objects.filter(id=self.request.user.id)

        @action(detail=True, methods=['GET'], permission_classes=[IsAuthenticated])
        def my_action(self, request, uuid=None):
            ....
            ....