sample_list = [i for i in range(10)]

# for loop
print([i*2 for i in sample_list])

# if(without else) + for loop
print([i for i in sample_list if i % 2 == 0])

# if else + for loop
print([i*2 if i % 2 == 0 else i for i in sample_list])

# test