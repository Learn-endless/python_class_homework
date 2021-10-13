# lst = ['张三', '李四', '王五', '赵六']
# # 查看列表中的数据
# print(lst)
# # 查看数据类型
# print(type(lst))
# # 索引
# name = lst[0]
# print(name)
# name = lst[3]
# print(name)
#
# print(len(lst))
# # 遍历列表
# for name in lst:
#     print(name)
# # 列表的增删改查
# # 增
# # 尾部增加数据 - lst.append(想增加的内容)
# lst.append('鲁七')
# print(lst)
#
# # 指定位置增加 - 两个参数，lst.insert(元素下标，想要增加的内容)
# lst.insert(0, '大王')
# print(lst)
#
# # 两个列表相加
# lst2 = ['刘邦', '李白', '鲁班', '兰陵王']
# lst3 = lst + lst2
# print(lst3)

# 列表删除
# lst = ['张三', '李四', '王五', '赵六']
# # lst.pop(2)  # 没有参数时，默认移除最后一个元素
# # print(lst)
# print(len(lst))
# lst.remove('李四') # 指定内容删除
# lst.clear() # 清除全部内容
# print(lst)

# # 修改操作
# lst[2] = '古力娜扎'
# print(lst)
#
# # 查询操作
# ret = lst.index('古力娜扎') # 根据内容获取索引值
# print(ret)

import time

lst = ['张三', '李四', '王五', '赵六']
for i in lst:
    print(i)
    time.sleep(3)
