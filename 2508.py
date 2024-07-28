import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    input()
    candyBox = []
    count = 0
    r, c = map(int,input().split())

    for _ in range(r):
        candyBox.append(list(input()))
    for i in range(r):
        for j in range(c):
            if candyBox[i][j] == '>' and j <= c-3:
                if candyBox[i][j+1] == 'o' and candyBox[i][j+2] == '<':
                    count +=1

            if candyBox[i][j] == 'v' and i <= r-3:
                if candyBox[i+1][j] == 'o' and candyBox[i+2][j] == '^':
                    count+=1 
    print(count)