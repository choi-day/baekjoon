N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start+end) // 2
    
    output = [j - mid for j in tree if j-mid > 0]

    if sum(output) >= M:
        start = mid + 1
    else:
        end = mid - 1
        
print(end)