from utilities.models import ContactMessage, Maintainer
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'


class MaintainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintainer
        fields = '__all__'
