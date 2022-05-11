
sample_list = [1,2,3]
big_sample_list = list()
sample_dict = dict()
sample_copy_list = sample_list.copy()

# list
big_sample_list.append(sample_list)

# dict
sample_dict["list_value"] = sample_list

print('value list clear 전:{}'.format(big_sample_list))
print('value list clear 전:{}'.format(sample_dict))

# value list clear
sample_list.clear()
print('value list clear 후:{}'.format(big_sample_list))
print('value list clear 후:{}'.format(sample_dict))

# item으로 추가한 list를 clear할 경우 다른 데이터에 모두 영향을 미친다
# 따라서 다른 데이터에 영향을 주지 않도록 아래와 copy()를 적극적으로 활용

# list
big_sample_list.append(sample_copy_list)

# dict
sample_dict["list_value"] = sample_copy_list

# value list clear
sample_list.clear()
print('value list clear 후:{}'.format(big_sample_list))
print('value list clear 후:{}'.format(sample_dict))
