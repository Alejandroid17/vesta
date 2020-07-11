from drf_yasg import openapi

query_parameter = openapi.Parameter(name='query',
                                    in_=openapi.IN_QUERY,
                                    required=False,
                                    default='',
                                    type=openapi.TYPE_OBJECT)
