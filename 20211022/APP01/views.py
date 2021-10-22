from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
# 1. 导入models模块
from APP01 import models

def hello(request):
    # 1. 查询person表格中所有的数据
    ret = models.Person.objects.all()
    return render(request, 'home.html', {'ret': ret})

# 添加用户，返回页面
def add(request):
    return render(request,'home_1.html')


# 添加用户，保存表单提交的数据
def add_person(request):
    # 1. 获取表单提交的内容
    username = request.POST.get('username')  # 获取表单提交的用户名
    age = request.POST.get('age')  # 获取表单提交的年龄
    print(username, age)
    # 2. 将获取的数据保存到数据库中
    person_obj = models.Person()
    person_obj.name = username
    person_obj.age = age
    person_obj.save()

    return render(request,'haha.html')
    # return redirect('http://127.0.0.1:8000/hello/')




