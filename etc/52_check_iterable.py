from collections.abc import Iterable

sample_object = {'a':1, 'b':2}
sample_tuple = ('a', 'b')
sample_list = ['a', 'b']
sample_string = 'ab'
sample_int = 1

# dict
if isinstance(sample_object, Iterable):
    print(True)

# tuple
if isinstance(sample_tuple, Iterable):
    print(True)
    
# list
if isinstance(sample_tuple, Iterable):
    print(True)

# string
if isinstance(sample_string, Iterable):
    print(True)
else:
    print(False)

# int
if isinstance(sample_int, Iterable):
    print(True)
else:
    print(False)