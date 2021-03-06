from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

a_router = DefaultRouter()
a_router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
a_router.register("profile", views.UserProfileViewSet)
a_router.register("feed", views.UserFeedView)

urlpatterns = [
    path("login/", views.UserLoginView.as_view()),
    path("hello-view/", views.HelloApiView.as_view()),
    path("api/", include(a_router.urls)),
]
