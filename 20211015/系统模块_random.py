import random  # 导入模块

# ret = random.random()  # 随机生成一个数

# ret = random.randint()  # 随机生成一个整数

# lst = [1, 2, 3, 4, 5, 6]
# ret = random.choice(lst)  # 随机从列表中选择一个数据
# print(ret)

# 生成验证码
def yzm():
    code = ''  # 保存生成的验证码
    for i in range(4):
        # 随机生成数字
        num = random.randint(0, 9)
        # 将整数强转成字符串
        num = str(num)
        # 随机生成数字（大写字母范围）加强转成字母
        zm = chr(random.randint(65, 90))
        # 随机生成数字（小写字符范围）加强转成字母
        pt = chr(random.randint(97, 122))
        # 随机生成的内容放到一个列表中
        lst = [num, zm, pt]
        # 随机拿取一个列表元素
        ret = random.choice(lst)
        # 将字符串拼接到code中
        code += ret
    # 循环四遍后，返回生成的四位验证码
    return code

Fhu = yzm()
print(Fhu)

'''
1. 需要使用random模块
2. 自定义模块名如果和系统的模块名一样，导入时，默认导入自己的。
'''

'''
srand((unsigned int)time(NULL));
int ret = rand();
printf("%d\n", ret);
'''
