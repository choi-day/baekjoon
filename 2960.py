#에라토스테네스의 체
n, k = map(int, input().split())

countK = 0
a = 0

isPrime = [True] * (n+1)

for i in range(2, n+1):
    if isPrime[i]:
        for j in range(i, n+1, i):
            if isPrime[j] == True:
                isPrime[j] = False
                countK += 1
                if countK == k:
                    a = j
                    break
print(a)