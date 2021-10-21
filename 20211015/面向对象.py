"""
类 和 对象
什么是 类 ： 对有相同特征和行为的事物的统称，是抽象的。
例子： 狗
行为： 汪汪叫
特征： 尾巴、鼻子、4条腿、白黄黑
代码中：属性表示特征，方法表示行为。
"""
class Dog:
    def jiao(self):
        print("汪汪叫...")
    def eat(self):
        print("吃骨头...")
    def notes(self):
        print("动动鼻子...")
    nose = "塌鼻子"
    tail = "短尾巴"
    leg = "四条腿"

# 创建对象（实例化对象）
dog_1 = Dog()
dog_1.jiao()
dog_1.eat()
dog_1.notes()
print(dog_1.leg)
print(dog_1.nose)
print(dog_1.tail)
print(Dog.nose)

