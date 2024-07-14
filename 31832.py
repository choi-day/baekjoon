import sys
input = sys.stdin.readline\

n = int(input())

for i in range(n):
    name = input().strip()
    up = 0
    down = 0
    for i in name:
        if i.isupper():
            up += 1
        elif i.islower():
            down += 1
    if down >= up:
        if len(name) <= 10:
            if name.isdigit() == False:
                print(name)
                break