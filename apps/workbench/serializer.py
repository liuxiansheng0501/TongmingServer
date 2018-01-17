# coding:utf-8
from rest_framework import serializers
from .models import child_archives,newborns,forty_two_days,five_six_month,one_year_old,two_year_old,three_year_old,four_year_old,five_year_old,six_year_old

class child_archives_serializer(serializers.ModelSerializer):
    class Meta:
        model=child_archives
        fields=('__all__')

class doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model=doctor
        fields=('account', 'passwd', 'name', 'hospital', 'type', 'title')

class hospital_serializer(serializers.ModelSerializer):
    class Meta:
        model = hospital
        fields = ('name', 'hospital', 'account', 'passwd', 'type')

# class child_archives_serializer(serializers.ModelSerializer):
#     class Meta:
#         model=child_archives
#         fields=('name', 'hospital', 'account', 'passwd', 'type')