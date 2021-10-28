from django.db import models

# Create your models here.

# 1.自己的类继承models.Model类后,Person类就能生成数据库表格
# 明显类
class Person(models.Model):
    name = models.CharField(max_length=32)  # name --->> varchar(32)
    age = models.IntegerField()    # age 是 int 类型

# 用户类
class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

# python manage.py check  检查模型类编写是否有问题
# python manage.py makemigrations  生成迁移文件
# python manage.py migrate  同步数据库  生成表格