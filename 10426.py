import datetime

day, gap = input().split()
y, m, d = map(int, day.split('-'))
dt = datetime.datetime(y,m,d)
dday = dt + datetime.timedelta(days = int(gap) -1 )
print(dday.strftime("%Y-%m-%d"))