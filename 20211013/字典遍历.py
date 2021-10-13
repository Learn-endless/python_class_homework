user_info_list = [{'name': '兰陵王', 'type': '刺客'},
                  {'name': '韩跳跳', 'type': '刺客'},
                  {'name': '嬴政', 'type': '法师'},
                  {'name': '鲁班', 'type': '射手'}, ]
for i in user_info_list:
    print(i['name'], '====', i['type'])
    # name = i['name']
    # types = i['type']
    # print(name, '====', types)

user_info = {'name': 'zs', 'age': 19, 'hobby': ['打篮球', '打游戏', '睡觉']}
ret = user_info['hobby'][1]
print(ret)
