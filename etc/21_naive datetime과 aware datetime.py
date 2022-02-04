# naive(애매한) datetime과 aware datetime에 대해 알아보자.
from datetime import datetime
from pytz import timezone

# naive datetime
now_date = datetime.now()

# aware datetime
kst = timezone('Asia/Seoul')
now_date_kst = now_date.replace(tzinfo=kst)

# compare date(naive)
sample_date = datetime(2012, 10, 9, 10, 10, 10)
print(sample_date < now_date)

# compare date(aware)
sample_date_kst = datetime(2012, 10, 9, 10, 10, 10, tzinfo=kst)
print(sample_date_kst < now_date_kst)

# cannot compare naive & aware date # typeerror
print(sample_date_kst < now_date)
