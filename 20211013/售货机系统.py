lst = ['手机', '电脑', '鼠标', '平板', 'U盘']
print('售货机系统'.center(31, "="))
for name in lst:
    ret = lst.index(name) + 1
    print("商品的序号：{0}，商品的名称：{1}".format(ret, name))
while True:
    number = input("请输入你要购买商品的序号(q/Q退出程序)：")
    print("-".center(34, "-"))
    if number.isdigit():
        if int(number) <= len(lst):
            s = lst[int(number) - 1]
            print("商品的序号：{0}，商品的名称：{1}".format(int(number), s))
            print('购买成功'.center(31, "-"))
        else:
            print("超出范围！")
    elif number.upper() == 'Q':  # number.lower() == 'q'
        print("退出程序!")
        break
    else:
        print("输入错误！")
