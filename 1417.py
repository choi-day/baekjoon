n = int(input())

a = []
for i in range(n):
    a.append(int(input()))
    
plus = 0

while(1):
    largeNum = 100
    largest = 0
    for i in range(n):
        if a[i] >= largest:
            largest = a[i]
            largeNum = i
    if largeNum == 0:
        print(plus)
        break
    else:
        a[largeNum] -= 1
        a[0] += 1
        plus += 1