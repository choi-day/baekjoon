e, f, c = map(int, input().split())
e = e + f
coke = 0

while True:
    coke = coke + e//c
    e = e%c + e//c
    if e < c:
        break

print(coke)