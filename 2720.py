import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    test = int(input())
    print(test // 25, end = ' ')
    test %= 25
    print(test // 10, end = ' ')
    test %= 10
    print(test // 5, end = ' ')
    print(test % 5)