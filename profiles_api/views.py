import rest_framework.request
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api.models import Feed, UserProfile
from profiles_api.permissions import (
    ProfileUpdatePermission,
    UpdateFeedPermission,
)


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
        """Entirely update an object."""
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        """Partially update an object."""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object."""
        return Response({"method": "DELETE"})


class HelloViewSet(ViewSet):
    """API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code",
        ]

        return Response({"message": "Hello!", "a_viewset": a_viewset})

    def create(self, request):
        """Create a hello message with a given name."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello, {name}!"
            return Response({"message": message})

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({"method": "GET"})

    def update(self, request, pk=None):
        return Response({"method": "PUT"})

    def partial_update(self, request, pk=None):
        return Response({"method": "PATCH"})

    def destroy(self, request, pk=None):
        return Response({"method": "DELETE"})


class UserProfileViewSet(ModelViewSet):
    """A view that handles creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ProfileUpdatePermission, IsAuthenticated)
    filter_backends = (SearchFilter,)
    search_fields = ("first_name", "last_name", "email")


class UserLoginView(ObtainAuthToken):
    """This view handles creations of user authentication tokens."""

    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class UserFeedView(ModelViewSet):
    """The view for the user's feeds."""

    serializer_class = serializers.UserFeedSerializer
    authentication_classes = [TokenAuthentication]
    queryset = Feed.objects.all()
    permission_classes = [UpdateFeedPermission, IsAuthenticated]

    def create(self, request: rest_framework.request.Request, *args, **kwargs):
        """
        Create a new Feed object when users send a POST request.

        :param request: the request from users.
        :type request: Request
        :return: a response with 201 status code or 400 if bad request.
        :rtype: Response
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.validated_data["user"] = request.user
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
