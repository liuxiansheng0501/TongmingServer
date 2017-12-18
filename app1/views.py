# coding:utf-8
import django_filters
from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import parent_user
from .serializer import parent_user_serializer

class parent_user_view_set(viewsets.ModelViewSet):
    queryset = parent_user.objects.all()
    serializer_class = parent_user_serializer
