from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serialize (convert) the request data into an object.
    The serializers in REST framework work very similarly to
    Django's Form and ModelForm classes.
    """

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a UserProfile object."""

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "first_name", "last_name", "password")
        # fields = ("email", "first_name", "last_name", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
            }
        }

    def create(self, validated_data):
        """Create a user."""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        """Update the user's password."""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)


class UserFeedSerializer(serializers.ModelSerializer):
    """The Serializer that serialize the Feed object."""

    class Meta:
        model = models.Feed
        fields = ["id", "user", "status_text", "created_on"]
        extra_kwargs = {
            "created_on": {"read_only": True},
            "user": {"read_only": True},
        }
