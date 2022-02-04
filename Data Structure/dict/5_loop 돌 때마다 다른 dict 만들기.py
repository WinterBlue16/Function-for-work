# 하나의 dict를 활용해 여러 개의 dict를 만들고, 저장한다.

users_list = []
sampled_dict = {
    'id': '',
    'name': ''
}
id_list = [1, 2, 3]
name_list = ['Alice', 'Ben', 'Sam']

# for loop without copy()
for i in range(len(id_list)):
    sampled_dict['id'] = id_list[i]
    sampled_dict['name'] = name_list[i]
    users_list.append(sampled_dict)

print(users_list)

# for loop with copy()
for i in range(len(id_list)):
    sampled_dict['id'] = id_list[i]
    sampled_dict['name'] = name_list[i]
    users_list.append(sampled_dict.copy())

print(users_list)
