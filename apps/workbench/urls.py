# coding=UTF-8

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^child_archives/new/$', views.save_child_archives, name='new child archives'),
    url(r'^child_archives/get/(?P<checked_child_id>.+)$', views.get_child_archives, name='get child archives'),
    url(r'^child_archives/idlist/$', views.get_child_idlist, name='get child idlist'),
    url(r'^child_archives/namelist/$', views.get_child_namelist, name='get child namelist'),
    url(r'^child_archives/unique/$', views.archives_unique, name='child archives unique valid'),
    url(r'^child_archives/update/$', views.save_child_archives, name='update child archives'),
    url(r'^newborns/new/$', views.save_newborns, name='new newborns'),
    url(r'^newborns/update/$', views.update_newborns, name='update newborns'),
    url(r'^newborns/get/(?P<checked_child_id>.+)$', views.get_newborns, name='get newborns'),
    url(r'^forty_two_days/new/$', views.save_forty_two_days, name='new forty_two_days'),
    url(r'^forty_two_days/update/$', views.save_forty_two_days, name='update forty_two_days'),
    url(r'^forty_two_days/get/(?P<checked_child_id>.+)$', views.get_forty_two_days, name='get forty_two_days'),
    url(r'^five_six_month/new/$', views.save_five_six_month, name='new five_six_month'),
    url(r'^five_six_month/update/$', views.save_five_six_month, name='update five_six_month'),
    url(r'^five_six_month/get/(?P<checked_child_id>.+)$', views.get_five_six_month, name='get five_six_month'),
    url(r'^one_year_old/new/$', views.save_one_year_old, name='new one_year_old'),
    url(r'^one_year_old/update/$', views.save_one_year_old, name='update one_year_old'),
    url(r'^one_year_old/get/(?P<checked_child_id>.+)$', views.get_one_year_old, name='get one_year_old'),
    url(r'^two_year_old/new/$', views.save_two_year_old, name='new two_year_old'),
    url(r'^two_year_old/update/$', views.save_two_year_old, name='update two_year_old'),
    url(r'^two_year_old/get/(?P<checked_child_id>.+)$', views.get_two_year_old, name='get two_year_old'),
    url(r'^three_year_old/new/$', views.save_three_year_old, name='new three_year_old'),
    url(r'^three_year_old/update/$', views.save_three_year_old, name='update three_year_old'),
    url(r'^three_year_old/get/(?P<checked_child_id>.+)$', views.get_three_year_old, name='get three_year_old'),
    url(r'^four_year_old/new/$', views.save_four_year_old, name='new four_year_old'),
    url(r'^four_year_old/update/$', views.save_four_year_old, name='update four_year_old'),
    url(r'^four_year_old/get/(?P<checked_child_id>.+)$', views.get_four_year_old, name='get four_year_old'),
    url(r'^five_year_old/new/$', views.save_five_year_old, name='new five_year_old'),
    url(r'^five_year_old/update/$', views.save_five_year_old, name='update five_year_old'),
    url(r'^five_year_old/get/(?P<checked_child_id>.+)$', views.get_five_year_old, name='get five_year_old'),
    url(r'^six_year_old/new/$', views.save_six_year_old, name='new six_year_old'),
    url(r'^six_year_old/update/$', views.save_six_year_old, name='update six_year_old'),
    url(r'^six_year_old/get/(?P<checked_child_id>.+)$', views.get_six_year_old, name='get six_year_old'),
    url(r'^query/doctor_checked/$', views.doctor_has_checked, name='doctor has checked'),
    url(r'^query/hospital_checked/$', views.hospital_has_checked, name='doctor has checked'),
]