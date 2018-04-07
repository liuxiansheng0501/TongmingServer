# coding=UTF-8

from django.conf.urls import url
from .views import *

urlpatterns=[
    url(r'^uncheckedlist/$', uncheck, name='un checked list'),#待检列表
    url(r'^uncheckedlist_doctor/$', uncheck_doctor, name='un checked list'),#待检列表
    url(r'^search/(?P<name>.+)$', match, name='search'),#模糊匹配搜索check
    url(r'^check/$', check, name='check'),#添加检查时间
    url(r'^new/$', new, name='search'),#产生新的预约
    url(r'^update/$', update, name='update'),#刷新预约
    url(r'^unique/$', queue_unique, name='queue unique'),#预约唯一性验证
]