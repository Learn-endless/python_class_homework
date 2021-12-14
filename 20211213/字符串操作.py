a = "小明"
b = 21
c = "学生"
print("我叫%s,我已经%d岁了，我还是一个%s" % (a, b, c))
print("我叫%s,我已经%d岁了，我还是一个%s" % ("小白", 22, "老师"))
print("我叫%s" % "hello word")

print("我叫{},我已经{}岁了，我还是一个{}".format(a, b, c))
print("我叫{0},我已经{1}岁了，我还是一个{2}".format(a, b, c))
print("我叫{name},我已经{age}岁了，我还是一个{id}".format(name=a, age=b, id=c))


Str = """这是一个多行字符串的实例
多行字符串可以使用制表符TAB(\t)。
也可以使用换行符[\n]。"""
print(Str)

x = 65
y = chr(x)
print("%c" % y)

s = "Affdsadd"
print(s.lower())  # 字符串转换为小写字符
print(s.upper())  # 字符串转换为大写字符

print(s.replace('ffd', 'X'))  # 将一个字符串替换成另一个字符串
lst = s.split('d')
for i in lst:
    print(i)
