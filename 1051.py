import sys

input = sys.stdin.readline

n, m = map(int,input().split())
square = []

for _ in range(n):
    num = input().rstrip()
    square.append(list(map(int, num)))

l = 1

for i in range(n-1):
    for j in range(m-1):
        for k in range(1, n+1):
            if(i+k >= n or j+k >= m):
                continue
            if(square[i][j] == square[i+k][j] and square[i][j] == square[i][j+k] and square[i][j] == square[i+k][j+k]):
                if(k+1 > l): l = k+1

print(l * l)