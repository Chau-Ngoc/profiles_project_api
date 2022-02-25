from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
