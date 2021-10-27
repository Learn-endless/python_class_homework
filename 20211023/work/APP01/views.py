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

    # return render(request,'haha.html')
    return redirect('http://127.0.0.1:8000/hello/')


# 删除用户
def del_person(request):
    # 获取 ID
    id = request.GET.get('id')
    # 删除数据库中个ID对应的数据
    models.Person.objects.get(id=id).delete()
    # 响应
    # return render(request,'haha.html')
    return redirect('http://127.0.0.1:8000/hello/')
    # return HttpResponse("删除成功")  # 视图函数


# 返回修改页面
def edit_person_html(request):
    # 1.获取id
    id = request.GET.get('id')
    # 2.查询数据库
    person_obj = models.Person.objects.get(id=id)\
    # 3.响应
    return render(request,'edit.html',{'person_obj': person_obj})


# 保存修改信息
def edit_person_post(request):
    # 1.获取表单提交的内容
    id = request.POST.get('id')
    username = request.POST.get('username')
    age = request.POST.get('age')
    # 2.查询数据库并且修改
    person_obj = models.Person.objects.get(id=id)
    person_obj.name = username
    person_obj.age = age
    person_obj.save()
    # 3.响应
    return redirect('http://127.0.0.1:8000/hello/')
