from datetime import datetime, timedelta

# present
today = datetime.now()
yesterday = today - timedelta(hours=24)
tomorrow = today + timedelta(hours=24)

# subtract
print(yesterday)
print((today - yesterday).days)

# add 
print(tomorrow)
print((tomorrow - today).days)
