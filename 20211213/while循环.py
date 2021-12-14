a = 0
while a <= 20:
    b = 0
    while b <= 33:
        c = 100-a-b  # 使用这个条件来将总数控制在100只
        if a*5+b*3+c/3 == 100:
            print(a, b, c)
        b += 1
    a += 1

n = 0
for i in range(10):
    if i % 3:
        print(i)
        continue
    n += 1
print(n)
