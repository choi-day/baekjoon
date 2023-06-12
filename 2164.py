n = int(input())
if(n == 1): li = [1]
else: li = list(range(2, n+1, 2))
if(n%2 == 0): check = 0
else: check = 1

while(len(li)!=1):
    a = li[len(li)-1]
    if(check == 0):
        del li[0::2]
    else:
        del li[1::2]
    if(a in li): check = 0
    else: check = 1
print(*li)