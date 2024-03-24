n = int(input())
k = int(input())

isPrime = [True] * (n+1)

for i in range(2, int(n**0.5)+1):
    if isPrime[i]:
        for j in range(2*i, n+1, i):
            isPrime[j] = False

kNum = [1]*(n+1)
for i in range(2, n+1):
    if isPrime[i] and i > k:
        for j in range(i, n+1, i):
            kNum[j] = 0
print(sum(kNum)-1)