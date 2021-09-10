from .models import Messages
from rest_framework import serializers


class MessageSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Messages
        fields = ['author', 'text']