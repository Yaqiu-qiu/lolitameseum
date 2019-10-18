from django.contrib import admin
# Register your models here.

from .models import UserInfo,Status,Skirt,Banner

@admin.register(Skirt)
class SkirtAdmin(admin.ModelAdmin):
    list_display = ('name','size','status','type','coverimg','image')
    #裙子列表里显示想要显示的字段
    list_per_page = 10
    #满10条数据就自动分



