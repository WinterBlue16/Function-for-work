import calendar


def get_month_last_day(year: int, month: int):
    month_last_day = calendar.monthrange(year, month)[-1]
    print("{}년 {}월의 마지막 날은 {}일입니다.".format(year, month, month_last_day))
    return month_last_day


get_month_last_day(2022, 6)
