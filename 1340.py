import sys

input = sys.stdin.readline

a={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,
'August':8,'September':9,'October':10,'November':11,'December':12}

month, day, year, hm = input().split(' ')
    
day = day[0:-1]
hh, mm = hm.split(':')
month = a[month]

day, year, hh, mm = int(day), int(year), int(hh), int(mm)

a=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if year%400==0 or (year%4==0 and year%100!=0):
    a[1]+=1

time=sum(a)*24*60
b=(sum(a[:month-1])+day-1)*24*60 + hh*60 + mm
print(b/time*100)