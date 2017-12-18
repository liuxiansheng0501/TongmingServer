# coding: utf-8

from rest_framework import routers
from .views import parent_user_view_set

router = routers.DefaultRouter()
router.register(r'parent_user', parent_user_view_set)