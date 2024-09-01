stroke = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

n , m = map(int,input().split())
a, b = input().split()
l = []
l2 = []
lest = ''

if len(a) < len(b):
    lest = b[len(a)::]
    b = b[0:len(a)]
elif len(a) > len(b):
    lest = a[len(b)::]
    a = a[0:len(b)]

for i, j in zip(a,b):
    l.append(i)
    l.append(j)

if len(lest) > 0:
    for i in lest:
        l.append(i)

for i in l:
    l2.append(stroke[(ord(i)-65)])

while(1):
    l3 = []
    if len(l2) == 2:
        if l2[0] == 0:
            print(str(l2[1])+'%')
        else:
            print(str(l2[0])+str(l2[1])+'%')
        break
    for i in range(0, len(l2)-1):
        l3.append((l2[i]+l2[i+1])%10)
    l2 = l3