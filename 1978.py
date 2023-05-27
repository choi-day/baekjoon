n = int(input())
li = list(map(int, input().split(' ')))
result = []
for i in li:
    if(i == 1): pass
    elif(i == 2): result.append(i)
    else:
        for j in range(2,i):
            if(i % j != 0):
                if(j == i-1): result.append(i)
            else: break
print(len(result))