n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b.sort(reverse=True)
c = []

for i in range(n):
    c.append(a[i]*b[i])
print(sum(c))