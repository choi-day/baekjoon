m, n = map(int, input().split())
 
array = []
result = 0
 
for i in range(m):
    array.append(list(map(int, input().split())))

for i in range(m):
    array_sort = sorted(array[i])
    temp = []
    for j in array[i]:
        temp.append(array_sort.index(j)+1)
    array[i] = temp
 
for i in range(m-1):
    for j in range(i+1, m):
        if array[i] == array[j]:
            result += 1
print(result)