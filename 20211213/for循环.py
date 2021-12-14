lst = ['apple', 'banana', 'peach']
for i in lst:
    print("列表元素：", i)

for i in 'Hello Word':
    print('当前字母为：', i)

for i in range(0, 10, 1):   # range的范围是 [ ) 左闭右开
    print(i)

i = 1
while i <= 3:
    print("外层循环i的值：%d" % i)
    i += 1
    j = 1
    while j <= 2:
        print("内层循环j的值：%d" % j)
        j += 1
