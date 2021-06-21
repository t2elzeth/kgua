from rest_framework import serializers

from .models import ApplicationDocument


class ApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocument
        fields = ["content"]
