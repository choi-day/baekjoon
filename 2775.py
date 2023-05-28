testNum = int(input())
for i in range(testNum):
    k = int(input())
    n = int(input())
    result = 0
    arr = [[0 for j in range(n)] for i in range(k+1)]
    for i in range(n):
        arr[0][i] = i+1
    for i in range(k+1):
        arr[i][0] = 1
    for i in range(1,k+1):
        for j in range(1, n):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[k][n-1])