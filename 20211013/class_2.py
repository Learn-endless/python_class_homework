# 字典: 用来存放事务的信息
# 键值对 key: value, key: value
user_info = {'name': '张三', 'age': 19, 'gender': '男'}
# print(user_info)
# print(type(user_info))
#
# # 字典的增删查改
# # 增加操作
# user_info['height'] = 185   # 不存在，增加
# print(user_info)
# user_info['height'] = 20    # 存在，修改值
# print(user_info)
# user_info.setdefault('weight', 120)  # 健存在，不修改，不存在，增加
# print(user_info)

# 删除操作
# user_info.clear()  # 清空字典
# user_info.pop('name')  # 根据键删除键值对
# print(user_info)

# user_info.popitem()  # 随机删除一个键值对
# print(user_info)

# i = 0
# while i < 20:
#     user_info = {'name': '张三', 'age': 19, 'gender': '男', 'height': 190}
#     user_info.popitem()
#     print(user_info)
#     i += 1

# 查询操作
name = user_info['name']
print(name)

age = user_info.get('agee')    # 如果见不存在，返回空 - None
print(age)
