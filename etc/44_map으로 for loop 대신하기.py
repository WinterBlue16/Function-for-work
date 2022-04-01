# for loop
sample_list = [i for i in range(10)]
new_sample_list = []
for i in sample_list:
    new_sample_list.append(i*i)
print(new_sample_list)

# map
new_sample_list = map(lambda i: i*i, sample_list)
print(new_sample_list)
