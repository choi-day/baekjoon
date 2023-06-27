import sys

n = int(sys.stdin.readline())
li = [int(sys.stdin.readline().strip()) for i in range(n)]
li_count = [0 for i in range(0, 8001)]
max_count = 0
li = sorted(li)

def roundUp(num):
    if(num > 0):
        if((num-int(num)) > 0.5):
            return int(num)+1
        else:
            return int(num)
    else:
        if((num-int(num)) > -0.5):
            return int(num)
        else:
            return int(num)-1
for i in li:
    li_count[i+4000] = li_count[i+4000]+1

if(li_count.count(max(li_count))<=1):
    max_count = li_count.index(max(li_count))-4000
else:
    m = li_count.index(max(li_count))
    max_count = li_count.index(max(li_count), m+1, len(li_count)-1)-4000
print(roundUp(sum(li)/n))
print(li[roundUp(n/2)])
print(max_count)
print(li[len(li)-1]-li[0])