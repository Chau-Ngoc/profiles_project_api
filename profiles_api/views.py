from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None) -> Response:
        """The HTTP GET request. Return a list of APIView features

        :param request: the HTTP request
        :type request: Request
        :param format: methods which create a request body
            such as post, put and patch, include a format argument,
            which make it easy to generate requests using a content
            type other than multipart form data. Available formats
            are 'multipart' and 'json', defaults to None
        :type format: str, optional
        :return: a HTTP response
        :rtype: Response
        """
        an_apiview = [
            "Uses HTTP methods as function (get, post, patch, put, delete)",
            "Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
            "Is mapped manually to URLs",
        ]
        return Response({"message": "Hello!", "an_apiview": an_apiview})

    def post(self, request):
        """A POST request that takes the user's name from the request
        data and return a hello message with that name.

        :param request: a HTTP request.
        :type request: Request
        :return: a HTTP response.
        :rtype: Response
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}!"
            return Response({"message": message})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        return Response({"method": "DELETE"})
