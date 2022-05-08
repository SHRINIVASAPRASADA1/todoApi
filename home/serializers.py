from rest_framework import serializers
from .models import todo


class todoserializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields ='__all__'
