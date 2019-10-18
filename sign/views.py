from django.shortcuts import render
from sign import models
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import auth
from sign.models import Skirt     #插入skirt表
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response



# Create your views here.

#def index(request):
   #   return render(request,'index.html')
def loginpage(request):
    return render(request,'login.html')
def regist(request):
    return render(request,'register.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method=='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        confirmpassword=request.POST.get('confirmpassword',None)
        if username and len(username)>6 and password and confirmpassword and confirmpassword==password:
            exist_flag=User.objects.filter(username=username).exists()
            if exist_flag:
                return HttpResponse('该用户已被注册')
            else:
                user=User.objects.create_user(username=username,password=password)
                return render(request,'index.html')
        else:
            return HttpResponse('账号密码格式不正确')

def login(request):
    if request.method=='POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username and len(username)>4 and password and len(password)>=6:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return render(request,'index.html')
            else:
                return HttpResponse('账号或密码错误！')
        else:
            return HttpResponse('账号或密码不符合规则')


def index(request):

    skirts=Skirt.objects.all() #将数据库中取出skirt表中的所有数据给skirts
   #return render(request,'table.html',{'form':table_form})

    return render_to_response("index.html",locals()) #必须用这个return

