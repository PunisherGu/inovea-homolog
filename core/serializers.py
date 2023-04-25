from rest_framework import serializers


class testserializer(serializers.Serializer):
    author = serializers.CharField()