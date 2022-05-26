import re

sample_string = "he\tll\no\n\n wo\trld!"

# solution 1
print(re.sub("\s+", "", sample_string))  # white space

# practice 1
print(re.sub("\s", "", sample_string))  # white space

# practice 2
print(re.sub("\t", "", sample_string))  # tab

# practice 3
print(re.sub("\n", "", sample_string))  # line break
