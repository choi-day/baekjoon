import sys

input = sys.stdin.readline

n =  int(input().strip())

list_a = list(map(int, input().split()))
sortedList_a = sorted(list_a)

# sortedList_a = {i:sortedList_a[i] for i in range(len(sortedList_a))}
# print(sortedList_a)

for i in list_a:
    print(sortedList_a.index(i), end=' ')
    sortedList_a[sortedList_a.index(i)] = 'x'