import ast

sample_string_list = "['a', 'b', 'c']"
convert_list = ast.literal_eval(sample_string_list)
print(type(sample_string_list))
print(type(convert_list))
