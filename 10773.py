import sys
n = int(input())
li = []
count = 0
while(count != n):
    m = int(sys.stdin.readline().strip())
    if(m == 0):
        if(len(li) == 0): break
        else: li.pop(len(li)-1)
    else: li.append(m)
    count = count + 1
if(len(li) == 0): print(0)
else: print(sum(li))