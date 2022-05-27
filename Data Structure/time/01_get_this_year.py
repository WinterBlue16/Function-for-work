from datetime import date


def get_this_year():
    return date.today().year


print("올해는 {}년입니다.".format(get_this_year()))
