from datetime import datetime

string_date_1 = "Dec, 01, 2021"
string_date_2 = "December, 01, 2021"

string_to_datetime1 = datetime.strptime(string_date_1, '%b, %d, %Y')
string_to_datetime2 = datetime.strptime(string_date_2, '%B, %d, %Y')

print(string_to_datetime1)
print(type(string_to_datetime1))

print(string_to_datetime2)
print(type(string_to_datetime2))
