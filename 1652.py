import sys
input = sys.stdin.readline

room = []
n = int(input())
for i in range(n):
    room.append(input().strip())
row = 0
col = 0
reversRoom = [[0 for j in range(n)] for i in range(n)]

for i in room:
    tmp = list(i.split('X'))
    for j in tmp:
        if len(j) >=2:
            col+=1
c = 0
for i in room:
    r = 0
    for j in i:
        reversRoom[r][c] = j
        r+=1
    c+=1

for i in reversRoom:
    tmp = list(''.join(i).split('X'))
    for j in tmp:
        if len(j) >= 2:
            row += 1
print(col, row)