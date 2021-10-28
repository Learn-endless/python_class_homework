"""work URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP01 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),   # 显示用户列表
    path('add/', views.add),        # 添加用户页面
    path('add_person/', views.add_person),   # 添加用户操作
    path('del_person/', views.del_person),    # 删除用户操作
    path('edit_person/', views.edit_person_html),  # 修改用户页面
    path('edit_person_post/', views.edit_person_post),  # 保存修改信息
    path('register_html/', views.register_html),   # 用户注册页面
    path('register_post/', views.register_post),   # 保存用户注册信息
    path('login_html/', views.login_html),   # 登录页面
    path('login_post/', views.login_post),   # 检验登录用户名
    path('set_cookie/', views.set_cookie),   # 创建cookie
    path('get_cookie/', views.get_cookie),   # 获取cookie
]
