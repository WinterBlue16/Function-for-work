from datetime import datetime

date_string = '13 May 2022'


def date_string_to_datetime(date_string):
    return datetime.strptime(date_string, '%d %B %Y')


print(date_string_to_datetime(date_string))
