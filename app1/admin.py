from django.contrib import admin
from .models import parent_user
# Register your models here.

@admin.register(parent_user)
class parent_user_admin(admin.ModelAdmin):
    pass


