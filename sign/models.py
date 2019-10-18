from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Create your models here.


class UserInfo(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    class Meta:
        db_table='user'


class Status(models.Model):
    name=models.IntegerField

class Skirt(models.Model):
    name=models.CharField(max_length=255)
    size=models.CharField(default=0,max_length=255)
    status=models.IntegerField(default=0)
    type=models.IntegerField(default=0)
    storeid=models.IntegerField(default=0)
    coverimg=models.ImageField('封面图',null=True,upload_to='coverimg/')
    image=models.ImageField('图',null=True,upload_to='photos/')

    #把路径显示成图片
   # def coverimg_data(self):
      #  return format_html(
      #      '<img src="{}" width="100px"/>',
     #       self.coverimg,
     #   )
    #coverimg_data.short_description='图片'

   # def coverimg_data(self, obj):

        #try:
           # coverimg = mark_safe('<img src="%s" width="50px" />' % (obj.file.url,))
        #except Exception as e:
           # coverimg = ''
        #return coverimg



class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图',null=True, upload_to='banner/')
    link_url = models.URLField('图片链接',null=True, max_length=100)
    is_active = models.BooleanField('是否是active', default=False)





