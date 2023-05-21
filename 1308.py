import datetime

today= input()
dday = input()

today = datetime.date(int(today.split(' ')[0]), int(today.split(' ')[1]), int(today.split(' ')[2]))
dday = datetime.date(int(dday.split(' ')[0]), int(dday.split(' ')[1]), int(dday.split(' ')[2]))
if (dday-today).days >= 365243 : print('gg')
else: print('D-',(dday-today).days, sep = '')