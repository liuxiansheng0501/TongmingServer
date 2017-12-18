from django.db import models
import django.utils.timezone as timezone

class parent_user(models.Model): #家长方用户
    card_id = models.CharField(max_length=30)  # 家长身份证号码
    name = models.CharField(max_length=20) # 家长姓名
    tele = models.IntegerField() # 家长手机号
    wechat_id = models.CharField(max_length=30)  # 微信ID
    account = models.CharField(max_length=20) # 账户名称
    passwd = models.CharField(max_length=20) # 账户密码

    def __str__(self):
        return self.name

class hospital_user(models.Model): # 医院方用户
    name = models.CharField(max_length=20) # 医生姓名
    hospital = models.CharField(max_length=30)  # 医生所在医院
    account = models.CharField(max_length=20)  # 账户名称
    passwd = models.CharField(max_length=20)  # 账户密码
    type = models.IntegerField() # 用户类型

    def __str__(self):
        return self.name

class hospital(models.Model): # 医院
    hos_id = models.IntegerField()  # 医院ID
    name = models.CharField(max_length=30)  # 医院名称
    admin_name = models.CharField(max_length=30)  # 管理员姓名
    admin_tele = models.CharField(max_length=30)  # 管理员联系方式
    account = models.CharField(max_length=20)  # 账户名称
    passwd = models.CharField(max_length=20)  # 账户密码
    def __str__(self):
        return self.name

class child_archives(models.Model): # 儿童眼保健档案
    child_id = models.CharField(max_length=30) # 儿童ID
    name=models.CharField(max_length=20) # 姓名
    sex=models.IntegerField() # 性别
    birthday= models.DateField(auto_now_add=False) # 出生年月
    parent_id= models.IntegerField() # 家长身份证号
    address=models.CharField(max_length=50) # 家庭住址
    gestational_age=models.IntegerField() # 出生胎龄
    weight_born = models.CharField(max_length=10) # 出生体重
    mother_pregnancy_history=models.CharField(max_length=200) # 母孕史
    past_medical_history=models.CharField(max_length=200) # 既往病史
    family_genetic_disease = models.CharField(max_length=200) # 家族遗传病史
    hospital = models.CharField(max_length=40) # 所属医院
    recorder = models.CharField(max_length=10) # 记录人
    record_datetime=models.DateTimeField(default = timezone.now) # 填写时间（含修改时间）
    def __str__(self):
        return self.name

class newborns(models.Model): # 新生儿（3--7天）眼保健情况记录
    newborns_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child=models.CharField(max_length=20) # 被检查新生儿姓名
    check_hospital=models.CharField(max_length=50) # 检查医院
    checker=models.CharField(max_length=10) # 检查人（医生或护士）
    check_datetime=models.DateTimeField(default = timezone.now) # 检查时间
    light_response=models.CharField(max_length=10) #光照反应
    optic_nystagmus=models.CharField(max_length=20) # 视动性眼震
    outer_eye_check = models.CharField(max_length=20) # 外眼检查
    pupil_reflects_on_light = models.CharField(max_length=20)  # 瞳孔对光反射
    reflex_red_eyes = models.CharField(max_length=20)  # 眼底红光反射
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class forty_two_days(models.Model): # 42天眼保健情况记录
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child=models.CharField(max_length=20) # 被检查新生儿姓名
    check_hospital=models.CharField(max_length=50) # 检查医院
    checker=models.CharField(max_length=10) # 检查人（医生或护士）
    check_datetime=models.DateTimeField(default = timezone.now) # 检查时间
    visual_behavior=models.CharField(max_length=10) #视觉行为
    outer_eye_check = models.CharField(max_length=20) # 外眼检查
    optic_nystagmus = models.CharField(max_length=20)  # 视动性眼震
    eye_sight_first_time_filter=models.CharField(max_length=10) # 视力初筛
    pupil_reflects_on_light = models.CharField(max_length=20)  # 瞳孔对光反射
    reflex_red_eyes = models.CharField(max_length=20)  # 眼底红光反射
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class five_six_month(models.Model): # 5-6个月眼保健情况记录
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child=models.CharField(max_length=20) # 被检查新生儿姓名
    check_hospital=models.CharField(max_length=50) # 检查医院
    checker=models.CharField(max_length=10) # 检查人（医生或护士）
    check_datetime=models.DateTimeField(default = timezone.now) # 检查时间
    visual_behavior=models.CharField(max_length=10) #视觉行为
    outer_eye_check = models.CharField(max_length=20) # 外眼检查
    optic_nystagmus = models.CharField(max_length=20)  # 视动性眼震
    infants_selective_gaze = models.CharField(max_length=20)  # 婴幼儿选择性注视
    reflex_red_eyes = models.CharField(max_length=20)  # 眼底红光反射
    eye_direction = models.CharField(max_length=20)  # 眼位检查
    nystagmus_check = models.CharField(max_length=20)  # 眼球震颤检查
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class one_year_old(models.Model):
    check_datetime = models.DateTimeField(default = timezone.now)  # 检查时间
    checker = models.CharField(max_length=10)  # 检查人（医生或护士）
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child = models.CharField(max_length=20)  # 被检查新生儿姓名
    check_hospital = models.CharField(max_length=50)  # 检查医院.
    visual_behavior = models.CharField(max_length=10)  # 视觉行为
    outer_eye_check = models.CharField(max_length=20)  # 外眼检查
    infants_selective_gaze = models.CharField(max_length=20)  # 婴幼儿选择性注视
    dot_vision_check=models.CharField(max_length=20)  # 点状视力检查
    reflex_red_eyes = models.CharField(max_length=20)  # 眼底红光反射
    refraction_check=models.CharField(max_length=20)  # 屈光检查
    eye_direction = models.CharField(max_length=20)  # 眼位检查
    nystagmus_check = models.CharField(max_length=20)  # 眼球震颤检查
    eye_x_check = models.CharField(max_length=20)  # 眼部超声
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class two_year_old(models.Model):
    check_datetime = models.DateTimeField(default = timezone.now)  # 检查时间
    checker = models.CharField(max_length=10)  # 检查人（医生或护士）
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child = models.CharField(max_length=20)  # 被检查新生儿姓名
    check_hospital = models.CharField(max_length=50)  # 检查医院.
    visual_behavior = models.CharField(max_length=10)  # 视觉行为
    outer_eye_check = models.CharField(max_length=20)  # 外眼检查
    infants_selective_gaze = models.CharField(max_length=20)  # 婴幼儿选择性注视
    dot_vision_check=models.CharField(max_length=20)  # 点状视力检查
    infant_vision_acuity_check = models.CharField(max_length=20)  # 婴幼儿视锐度检查
    reflex_red_eyes = models.CharField(max_length=20)  # 眼底红光反射
    refraction_check=models.CharField(max_length=20)  # 屈光检查
    eye_direction = models.CharField(max_length=20)  # 眼位检查
    nystagmus_check = models.CharField(max_length=20)  # 眼球震颤检查
    eye_x_check = models.CharField(max_length=20)  # 眼部超声
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class three_year_old(models.Model):
    check_datetime = models.DateTimeField(default = timezone.now)  # 检查时间
    checker = models.CharField(max_length=10)  # 检查人（医生或护士）
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child = models.CharField(max_length=20)  # 被检查新生儿姓名
    check_hospital = models.CharField(max_length=50)  # 检查医院.
    visual_behavior = models.CharField(max_length=10)  # 视觉行为
    eye_sight_check = models.CharField(max_length=10)  # 视力检查
    dot_vision_check=models.CharField(max_length=20)  # 点状视力检查
    children_graphics_vision_card = models.CharField(max_length=20)  # 儿童图形视力卡
    infant_vision_acuity_check = models.CharField(max_length=20)  # 婴幼儿视锐度检查
    outer_eye_anterior_segment_check = models.CharField(max_length=20)  # 外眼及眼前节检查
    refraction_check=models.CharField(max_length=20)  # 屈光检查
    eye_direction = models.CharField(max_length=20)  # 眼位检查
    nystagmus_check = models.CharField(max_length=20)  # 眼球震颤检查
    fundus_check = models.CharField(max_length=20)  # 眼底检查
    eye_x_check = models.CharField(max_length=20)  # 眼部超声
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class four_year_old(models.Model):
    check_datetime = models.DateTimeField(default = timezone.now)  # 检查时间
    checker = models.CharField(max_length=10)  # 检查人（医生或护士）
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child = models.CharField(max_length=20)  # 被检查新生儿姓名
    check_hospital = models.CharField(max_length=50)  # 检查医院.
    visual_behavior = models.CharField(max_length=10)  # 视觉行为
    eye_sight_check = models.CharField(max_length=10)  # 视力检查
    dot_vision_check=models.CharField(max_length=20)  # 点状视力检查
    children_graphics_vision_card = models.CharField(max_length=20)  # 儿童图形视力卡
    outer_eye_anterior_segment_check = models.CharField(max_length=20)  # 外眼及眼前节检查
    refraction_check=models.CharField(max_length=20)  # 屈光检查
    eye_direction = models.CharField(max_length=20)  # 眼位检查
    nystagmus_check = models.CharField(max_length=20)  # 眼球震颤检查
    fundus_check = models.CharField(max_length=20)  # 眼底检查
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class five_year_old(models.Model):
    check_datetime = models.DateTimeField(default = timezone.now)  # 检查时间
    checker = models.CharField(max_length=10)  # 检查人（医生或护士）
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child = models.CharField(max_length=20)  # 被检查新生儿姓名
    check_hospital = models.CharField(max_length=50)  # 检查医院.
    visual_behavior = models.CharField(max_length=10)  # 视觉行为
    eye_sight_check = models.CharField(max_length=10)  # 视力检查
    dot_vision_check = models.CharField(max_length=20)  # 点状视力检查
    children_graphics_vision_card = models.CharField(max_length=20)  # 儿童图形视力卡
    outer_eye_anterior_segment_check = models.CharField(max_length=20)  # 外眼及眼前节检查
    refraction_check = models.CharField(max_length=20)  # 屈光检查
    eye_direction = models.CharField(max_length=20)  # 眼位检查
    nystagmus_check = models.CharField(max_length=20)  # 眼球震颤检查
    fundus_check = models.CharField(max_length=20)  # 眼底检查
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class six_year_old(models.Model):
    check_datetime = models.DateTimeField(default = timezone.now)  # 检查时间
    checker = models.CharField(max_length=10)  # 检查人（医生或护士）
    checked_child_id = models.CharField(max_length=30)  # 被检查新生儿ID
    checked_child = models.CharField(max_length=20)  # 被检查新生儿姓名
    check_hospital = models.CharField(max_length=50)  # 检查医院.
    visual_behavior = models.CharField(max_length=10)  # 视觉行为
    eye_sight_check = models.CharField(max_length=10)  # 视力检查
    outer_eye_anterior_segment_check = models.CharField(max_length=20)  # 外眼及眼前节检查
    refraction_check = models.CharField(max_length=20)  # 屈光检查
    eye_direction = models.CharField(max_length=20)  # 眼位检查
    nystagmus_check = models.CharField(max_length=20)  # 眼球震颤检查
    fundus_check = models.CharField(max_length=20)  # 眼底检查
    other_item = models.CharField(max_length=20)  # 其他检查
    is_cooperation = models.CharField(max_length=20)  # 检查合作
    result = models.CharField(max_length=20)  # 检查结论
    suggestion = models.CharField(max_length=20)  # 医学意见
    def __str__(self):
        return self.name

class login_record(models.Model):#登录记录表
    user=models.CharField(max_length=20) # 姓名
    hospital=models.CharField(max_length=50) # 医院
    login=models.DateTimeField(default = timezone.now) # 登录时间
    logout=models.DateTimeField(default = timezone.now) # 登出时间



