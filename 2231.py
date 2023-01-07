n = int(input())
nSum = 0
conArray = []

for i in range(n):
    nlist = [int(j) for j in str(i)]
    nSum = i + sum(nlist)
    if(nSum == n):
        conArray.append(i)

if(len(conArray) == 0):
    print(0)
else:
    print(min(conArray))