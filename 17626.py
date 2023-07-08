#이 풀이도 맞지만 시간과 메모리를 두 배로 소요

# k = int(input())

# d = [[0 for j in range(k+1)] for i in range(223+1)]

# for i in range(1, k+1):
#     d[1][i] = i

# for sqr in range(2, 223+1):
#     for n in range(1, k+1):
#         if(sqr*sqr > n): d[sqr][n] = d[sqr-1][n]
#         else:
#             d[sqr][n] = min(int(n/(sqr*sqr)) + d[sqr-1][n%(sqr*sqr)], d[sqr-1][n])
# print(d[223][k])

import math
 
n = int(input())
dp = [0,1]
 
for i in range(2, n+1):
    minValue = 1e9
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j**2])
    dp.append(minValue + 1)
 
print(dp[n])