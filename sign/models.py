from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    class Meta:
        db_table='user'
