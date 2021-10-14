# 1.模块的导入方式：2种
# 第一种方式： import
# 第二种方式： from 模块名称 import 变量

# 导入模块model_1
# import model_1
# # 调用格式： 模块名.XXX
# ret = model_1.name   # 调用模块中的变量
# print(ret, end='')
#
# model_1.say_hello()   # 调用模块中的函数
#
#
# print('模块')

# 用from方式导入模块
from model_1 import name, say_hello

name_1 = name
print(name_1)
say_hello()
print('模块...')
