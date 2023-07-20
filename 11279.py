from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input().strip())
heap = []

for _ in range(n):
    i = int(input().strip())
    if(i == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (-i, i))