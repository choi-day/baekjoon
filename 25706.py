import sys
input = sys.stdin.readline

# 입력
n = int(input().strip())
jumps = list(map(int, input().split()))

# dp 배열 초기화
dp = [1] * n

# 뒤에서부터 계산
for i in range(n - 2, -1, -1):
    if i + jumps[i] + 1 < n:
        dp[i] = dp[i + jumps[i] + 1] + 1

# 결과 출력
print(" ".join(map(str, dp)))