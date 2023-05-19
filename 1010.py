import itertools

T = int(input())
n = []
m = []
for i in range(0, T):
    a, b = map(int, input().split())
    n.append(a)
    m.append(b)

def combinations(n, r):
    return mul(n) // (mul(r) * mul(n - r))

def mul(k):
    prod = 1
    for i in range(1, k + 1):
        prod *= i
    return prod

for i in range(T):
    if n[i] == m[i]:
        print(1)
    else:
        print(combinations(m[i], n[i]))

# 콤비네이션 쉽게 구현하기

#     for i in range(M, M-N,-1):
#         a *= i
    
#     for j in range(N,1,-1):
#         b *= j
#     print(int(a/b))