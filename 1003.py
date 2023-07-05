d = [[0 for j in range(41)] for i in range(2)]
d[0][0] = 1
d[1][0] = 0
d[0][1] = 0
d[1][1] = 1

t = int(input())
for i in range(t):
    n =  int(input())
    for i in range(2, n+1):
        if(d[0][i] == 0): d[0][i] = d[0][i-1] + d[0][i-2]
        if(d[1][i] == 0): d[1][i] = d[1][i-1] + d[1][i-2]
    print(d[0][n], d[1][n])