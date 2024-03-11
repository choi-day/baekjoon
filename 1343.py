import sys

input = sys.stdin.readline

board = input()
a=[]

countX = 0

for i in board:
    if i == 'X':
        countX += 1
    else:
        if(countX % 2 == 1):
            a = [-1]
            break
        else:
            a.append('A'*(int(countX/4)*4))
            a.append('B'*int(countX%4))
            countX=0
            if i == '.':
                a.append('.')
if len(a) == 1:
    print(a[0])
else:
    print(''.join(a))