n = int(input())
count = 0

for i in range(n):
    word = input()
    array = []
    for j in word:
        if(len(array) == 0): array.append(j)
        elif(array[len(array)-1] == j): pass
        else: array.append(j)
    if(len(array) == len(set(array))): count=count+1
print(count)