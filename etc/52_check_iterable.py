from collections.abc import Iterable

sample_object = {'a':1, 'b':2}

if isinstance(sample_object, Iterable):
    print(True)