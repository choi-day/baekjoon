import sys
input = sys.stdin.readline

n = int(input())
l = list(input().strip())
m = int(input())
s = input().strip()
count = 0
b = 0
k = n-1

for i in s:
    if i not in l:
        b = 1
        break
    else:
        while(1):
            count += 1
            k += 1
            if l[k%n] == i:
                break
            else:
                pass
if b == 0:
    print(count)
else:
    print(-1)