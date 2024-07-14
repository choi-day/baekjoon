n = int(input())
sList = sorted(list(map(int, input().split())))

count = 0
b = 0

for i in sList:
    if b < i:
        count += 1
        b = i
        sList.remove(i)

b = 1001

for i in sList[::-1]:
    if b > i:
        count += 1
        b = i
        sList.remove(i)

print(count)