import sys
n, m= map(int, sys.stdin.readline().strip().split(' '))
dict = {}
for i in range(1, n+1):
    a = sys.stdin.readline().strip()
    dict[i] = a
    dict[a] = i

for _ in range(m):
    test = sys.stdin.readline().strip()
    if(test.isdigit()):
        print(dict[int(test)])
    else:
        print(dict[test])