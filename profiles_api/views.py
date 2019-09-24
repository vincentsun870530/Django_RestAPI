from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP methods as fucntion (get, post, patch, put, delete)'
        ]


        return Response({'message':'Hello!', 'an_apiview' : an_apiview})