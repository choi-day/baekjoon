n = int(input()) - 1
count = 0
for i in range(0, n, 6):
    n = n - i
    if(n > 0):
        count = count + 1
    else:break
print(count+1)