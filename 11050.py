n, k = list(map(int, input().split(' ')))
result = 1
# if(n == 0) : print(1)
# else:
if(n-k > k): k = n-k
for i in range(k+1, n+1):
    result = result * i
for i in range(1, n-k+1):
    result = result / i
print(int(result))