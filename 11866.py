from collections import deque
n, k = list(map(int, input().split(' ')))
q = deque(list(range(1, n+1)))
result = []

while((len(result)) != n):
    q.rotate(-(k-1))
    a = q.popleft()
    result.append(a)
print('<' + ", ".join([str(i) for i in result]) + '>')