from django.shortcuts import render

# Create your views here.
# 1. 导入models模块
from APP01 import models

def hello(request):
    # 1. 查询person表格中所有的数据
    ret = models.Person.objects.all()
    print(ret)  # 列表类型
    for temp in ret:
        print(temp.name,'-->>',temp.age)
    return render(request, 'home.html', {'ret': ret})
