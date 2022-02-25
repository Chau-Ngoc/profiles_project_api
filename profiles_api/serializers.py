from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialize (convert) the request data into an object.
    The serializers in REST framework work very similarly to
    Django's Form and ModelForm classes.
    """

    name = serializers.CharField(max_length=10)
