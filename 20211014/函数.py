# # 函数的作用：提高代码的中用率
# # 定义函数
# def say_hello():       # say_hell : 函数名
#     """
#     this is a func ， 作用是say hello
#     :return: 函数的返回值，默认是None
#     """
#     print("hello world!!!")
#
# # 定义一个加法函数
# def add(a, b):
#     return a+b
#
# print(add(1, 2))
#
# # 函数调用
# say_hello()
# say_hello()
# # 注意：函数声明一次，可以调用多次

# 编写带参数的函数
# def say_hello2(msg):
#     print(msg)

# say_hello2('hello 东湖学院')

# def say_hello3(msg1, msg2):
#     print(msg1, msg2)
#
# # say_hello3('你好啊', '帅哥啊')
#
#
# say_hello3('么么哒')  # 参数数量不匹配，报错


# 1.形参 （位置参数）
# 2.默认参数(形式参数有默认值)
# def get_info(name, age, gender='男'):
#     # 注意{}是英文的！！！
#     print("大家好，我的名字叫：{},年龄：{:10,.2f},性别：{}".format(name.rjust(20), age, format(gender, '>20')))

# # 当函数有实际参数时，使用传递的实际参数值
# get_info('张三', 20, '女')
# get_info('李四', 21, '男')
# # 当函数没有实际参数时，使用默认值(前提是定义函数的形式参数有默认值)
# get_info('王五', 22)

# 3.使用关键字传参(关键字来源于形参)
# get_info(gender='女', name='大佬', age=30.1314526)

# 字符串右对齐函数.rjust(总的占位数)
# test = "hello world"
# print(test.rjust(20))


# 4.可变参数
# *args：接受位置的参数
# **kwargs: 接受关键字的参数

# def say_hello4(*args):
#     print(args)
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#
# say_hello4('hello', '你好', '亚麻跌', '再见大海')

# def say_hello5(**kwargs):
#     print(kwargs)
#     print(kwargs['taiyu'])  # 通过字典的操作，索引键名位taiyu的值
# say_hello5(taiyu='萨瓦迪卡', hanyu='阿尼')
#
# # 函数的返回值
# def say_hello6(msg):
#     print('lalala')
#     return msg
#
# # 用变量接收返回值
# aa = say_hello6('你好')
# print(aa)


# 返回多个值
# def say_hello7(msg1, msg2):
#     return msg1, msg2
#
# ret = say_hello7('hello', 'sa wa di ka')
# print(ret)
# # print(ret[1])  # 列表操作



# 给函数传递一个值n，然后求n的阶乘，并且将值返回。

def Factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

while True:
    number = int(input("请输入一个整数："))
    if number <= 0:
        print('退出程序')
        break
    else:
        print(Factorial(number))

