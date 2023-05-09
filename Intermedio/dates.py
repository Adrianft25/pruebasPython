from datetime import datetime

now = datetime.now()

timestamp = now.timestamp()

print(timestamp)

y2024 = datetime(2024, 10, 14)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
print_date(y2024)

from datetime import time

currentTime = time()
