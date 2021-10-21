# 1. 导入模块
from django.shortcuts import HttpResponse, render


# 2. 创建视图函数
def hello(request):
    return HttpResponse("Hello World")


# 返回index.html页面
def index(request):
    return render(request, 'index.html')


def index1(request):
    name = "尼古拉斯"
    age = 19
    game_lst = ['LOL','CF','DNF']
    return render(request, "index1.html", {'name': name, 'age': age, 'game_lst': game_lst})


