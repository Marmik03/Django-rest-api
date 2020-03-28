from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    def get(self, request , format=None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP Mthod as function (get, post, put, delete)',
            'It is similatr to traditional django view',
            'is mapped manually to URLs',
            'Gives you the most control',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
