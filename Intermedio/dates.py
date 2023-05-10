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

currentTime = time(22,5,0)

print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)

from datetime import date

currentDate = date.today()

print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

currentDate2 = date(1998,10,14)

print(currentDate2.year)
print(currentDate2.month)
print(currentDate2.day)


# Operaciones con dates

currentDate3 = date(currentDate2.year + 4, currentDate2.month - 1, currentDate2.day) 

print(currentDate3.year)
print(currentDate3.month)
print(currentDate3.day)

# Operaciones entre datetimes y times

diff = y2024 - now
print(diff)

diff2 = y2024.date() - currentDate3
print(diff2)

from datetime import timedelta

start = timedelta(200,100,250,weeks=10)
end = timedelta(300,100,250,weeks=27)

print(end - start)
print(end + start)
# NO SE PUEDE HACER         print(end * start)
# SI, PERO NO TIENE SENTIDO print(end / start)

