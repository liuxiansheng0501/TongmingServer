# coding=UTF-8
from rest_framework import serializers
from .model import queue

class queue_serializer(serializers.ModelSerializer):
    class Meta:
        model=queue
        fields=('__all__')

class queue_unique_serializer(serializers.ModelSerializer):
    class Meta:
        model=queue
        fields=(['child_name','parent_id'])