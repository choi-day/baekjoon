import sys
input = sys.stdin.readline

n = int(input())
book = {}
for _ in range(n):
    a = input().strip()
    if a in book:
        book[a] += 1
    else:
        book[a] = 1

book = sorted(book.items(), key = lambda item: item[1])
best = []

for i in book:
    if i[1] == book[len(book)-1][1]:
        best.append(i[0])
best =  sorted(best)

print(best[0])