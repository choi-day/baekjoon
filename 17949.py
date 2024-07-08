q = input()
n = int(input())
type = list(input().split())
typeSize = [0]
sliceQ = []

for i in type:
    if i == 'int':
        typeSize.append(8)
    elif i == 'char':
        typeSize.append(2)
    else:
        typeSize.append(16)

for i in range(len(typeSize)-1):
    typeSize[i+1] = typeSize[i]+typeSize[i+1]
    sliceQ.append(q[typeSize[i]:typeSize[i+1]])

for i in sliceQ:
    print(int(i, 16), end=' ')