from rest_framework import serializers

from main.models import BaseProcess


class BaseProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProcess
        fields = "__all__"
