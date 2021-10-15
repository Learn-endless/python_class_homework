# class Person:
#     def eat(self):
#         print(self.name, '说：食堂的饭比较难吃...')

# per = Person()
# per.name = '王五'
# per.eat()
#
# per_1 = Person()
# per_1.name = '赵四'
# per_1.eat()

# 使用魔术方法
class Dog:
    def __init__(self, value):
        """
        对象初始化的魔术方法：创建对象的时候会自动执行。
        """
        print("init...")
        self.name = value   # 将形参value的值给对象的name属性
    def eat(self):
        print(self.name, "吃骨头...")  # 调用对象的name属性

dog = Dog('小白')
dog.eat()

dog = Dog('小黑')
dog.eat()

