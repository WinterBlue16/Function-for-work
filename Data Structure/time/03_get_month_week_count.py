import calendar


def get_month_week_count(year: int, month: int):
    month_week_count = len(calendar.monthcalendar(year, month))
    print("{}년 {}월은 전체 {}주입니다.".format(year, month, month_week_count))
    return month_week_count


get_month_week_count(2022, 6)
