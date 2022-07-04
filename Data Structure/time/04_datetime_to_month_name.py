from datetime import datetime


def month_number_to_month_name(month_number: int):
    month_object = datetime.strptime(str(month_number), "%m")
    month_name_short = month_object.strftime("%b")
    month_name_full = month_object.strftime("%B")
    return month_name_short, month_name_full


print(month_number_to_month_name(4))
