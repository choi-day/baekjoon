n = int(input())

p = [0 for i in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(4, 101):
    p[i] = p[i-2] + p[i-3]
for _ in range(n):
    m = int(input())
    print(p[m])