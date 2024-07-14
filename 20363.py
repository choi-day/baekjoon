x, y = map(int, input().split())

if x >= y:
    sun = x + y // 10
    water = y
else:
    water = y + x // 10
    sun = x

print(sun+water)