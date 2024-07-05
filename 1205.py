import sys
input = sys.stdin.readline

n, new, p = map(int, input().split())
rank = []
if(n!=0):
    i =  sorted(list(map(int, input().split())), reverse=True)
for _ in range(n):
    for j in i:
        if len(rank) < n:
            rank.append(j)
        else:
            break
new_rank = 1

if len(rank) == 0:
    print(1)
elif new <= rank[len(rank)-1] and len(rank) >= p:
    print(-1)
else:
    for i in rank:
        if new < i:
            new_rank += 1
        else:
            break
    print(new_rank)