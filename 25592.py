n = int(input())
if n == 1:
    need = 0
elif n == 2:
    need = 0
elif n == 3:
    need = 3
now = n

for i in range(1, n):
    if(now >= i):
        now -= i
    else:
        if(i % 2 == 1):
            need = i - now
            break
        else:
            need = 0
            break
print(need)