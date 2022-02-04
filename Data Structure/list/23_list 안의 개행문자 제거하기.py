'''
list 혹은 string에 포함된 '\n' 등의 개행문자를 제거한다. 
'''

# string
sample_str = 'Hello world!\n'
print('개행문자 제거 전:{}'.format(sample_str))
print('개행문자 제거 후:{}'.format(sample_str.rstrip()))

# list
sample_list = ['This\n', 'is\n', 'test\n']
for s in sample_list:
    print(s)

sample_list = [s.strip() for s in sample_list]
print('개행문자 제거 후:{}'.format(sample_list))
