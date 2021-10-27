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
    path('edit_person_post/', views.edit_person_post),
]
