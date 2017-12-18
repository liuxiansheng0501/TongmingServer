# coding:utf-8
from rest_framework import serializers
from .models import parent_user

class parent_user_serializer(serializers.ModelSerializer):
    class meta:
        model=parent_user
        fields=('name','tele')