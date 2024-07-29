import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n, m = input().split()
    n, m = list(n), list(m)
    count = 0
    diff = []

    for i in range(len(n)):
        if n[i] != m[i]:
            diff.append(n[i])
    zero = diff.count('0')
    one = diff.count('1')
    print(max(zero, one))