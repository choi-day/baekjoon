import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    mod = list(input().strip())

    if '1' in mod:
        num = 1
        numIn = mod.index('1')
        left = len(mod[0:numIn])
        right = len(mod[numIn:len(mod)])
        print(1 if left % 2 == 0 else 0)
    else:
        num = 0
        numIn = mod.index('0')
        left = len(mod[0:numIn])
        right = len(mod[numIn:len(mod)])
        if right > 1:
            num = 1
            print(1 if left % 2 == 0 else 0)
        else:
            print(0 if left % 2 == 0 else 1)