from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self, request , format=None):
        """Returns a list of API View features"""
        an_apiview = [
            'Uses HTTP Mthod as function (get, post, put, delete)',
            'It is similatr to traditional django view',
            'is mapped manually to URLs',
            'Gives you the most control',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """"Create a Hello Message with Our Name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request , pk = None):
        """Handling updating an object """
        return Response({'method':'PUT'})

    def patch(self, request , pk = None):
        """Handling partial update of an object """
        return Response({'method':'PATCH'})

    def delete(self, request , pk = None):
        """Deleting an object """
        return Response({'method':'DELETE'})
