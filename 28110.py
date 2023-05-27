n = int(input())
result = 0
diff = 0

array = sorted(list(map(int, input().split(' '))))

for i in range(0, n-1):
    if(int((array[i+1]-array[i])/2) > diff):
        result = array[i] + int((array[i+1]-array[i])/2)
        diff = int((array[i+1]-array[i])/2)

if(result == 0): print(-1)
else: print(result)