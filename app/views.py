from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def hello(request):
    return HttpResponse('hello world')


# 首页
def index(request):
    return render(request, 'index.html')


# 联系我
def callme(request):
    return render(request,'callme.html')


# 写文章
def write(request):
    return render(request,'write.html')


# 登录
def login(request):
    return render(request,'login.html')


# 退出
def logout(request):
    return redirect('/index/')


# 注册
def register(request):
    return render(request,'register.html')
