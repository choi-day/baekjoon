n, j, h = map(int, input().split())

count = 0

while j != h:
    j -= (j//2)
    h -= (h//2)
    count += 1
print(count)