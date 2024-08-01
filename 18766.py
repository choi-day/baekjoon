import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    before = sorted(list(input()))
    after = sorted(list(input()))

    if before == after:
        print('NOT CHEATER')
    else:
        print('CHEATER')