# coding:utf-8
from rest_framework import serializers
from .models import queue

class queue_serializer(serializers.ModelSerializer):
    class Meta:
        model=queue
        fields=('__all__')