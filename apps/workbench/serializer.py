# coding=UTF-8
from rest_framework import serializers
from .model import *

class child_archives_serializer(serializers.ModelSerializer):
    class Meta:
        model=child_archives
        fields=('__all__')

class child_archives_id_list_serializer(serializers.ModelSerializer):
    class Meta:
        model=child_archives
        fields=(['child_id'])

class child_archives_unique_serializer(serializers.ModelSerializer):
    class Meta:
        model=child_archives
        fields=(['child_id','child_name','parent_id'])

class child_archives_name_list_serializer(serializers.ModelSerializer):
    class Meta:
        model=child_archives
        fields=(['child_id','child_name','parent_name'])

class newborns_serializer(serializers.ModelSerializer):
    class Meta:
        model=newborns
        fields = ('__all__')

class forty_two_days_serializer(serializers.ModelSerializer):
    class Meta:
        model = forty_two_days
        fields = ('__all__')

class five_six_month_serializer(serializers.ModelSerializer):
    class Meta:
        model = five_six_month
        fields = ('__all__')

class one_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = one_year_old
        fields = ('__all__')

class two_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = two_year_old
        fields = ('__all__')

class three_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = three_year_old
        fields = ('__all__')

class four_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = four_year_old
        fields = ('__all__')

class five_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = five_year_old
        fields = ('__all__')

class six_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = six_year_old
        fields = ('__all__')

class query_newborns_serializer(serializers.ModelSerializer):
    class Meta:
        model = newborns
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_forty_two_days_serializer(serializers.ModelSerializer):
    class Meta:
        model = forty_two_days
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_five_six_month_serializer(serializers.ModelSerializer):
    class Meta:
        model = five_six_month
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_one_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = one_year_old
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_two_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = two_year_old
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_three_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = three_year_old
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_four_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = four_year_old
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_five_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = five_year_old
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_six_year_old_serializer(serializers.ModelSerializer):
    class Meta:
        model = six_year_old
        fields = (['check_datetime','checked_child_name','checked_child_parent_name','result'])

class query_newborns_serializer2(serializers.ModelSerializer):
    class Meta:
        model = newborns
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_forty_two_days_serializer2(serializers.ModelSerializer):
    class Meta:
        model = forty_two_days
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_five_six_month_serializer2(serializers.ModelSerializer):
    class Meta:
        model = five_six_month
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_one_year_old_serializer2(serializers.ModelSerializer):
    class Meta:
        model = one_year_old
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_two_year_old_serializer2(serializers.ModelSerializer):
    class Meta:
        model = two_year_old
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_three_year_old_serializer2(serializers.ModelSerializer):
    class Meta:
        model = three_year_old
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_four_year_old_serializer2(serializers.ModelSerializer):
    class Meta:
        model = four_year_old
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_five_year_old_serializer2(serializers.ModelSerializer):
    class Meta:
        model = five_year_old
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])

class query_six_year_old_serializer2(serializers.ModelSerializer):
    class Meta:
        model = six_year_old
        fields = (['check_datetime','check_hospital_name','checked_child_name','check_doctor_name','checked_child_parent_name','result'])