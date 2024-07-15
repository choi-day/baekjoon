a ,b = input().split()

listA = list(a)
listB = list(b)
blequal = 0

for i in range(len(listA)):
    for j in range(i, len(listB)-len(listA)+i+1):
        if listA[i] == listB[j]:
            equal = 1
            k =  i+1
            l = j+1
            while(k < len(listA)):
                if listA[k] == listB[l]:
                    equal += 1
                k += 1
                l += 1
            if blequal < equal:
                blequal = equal
print(len(a)-blequal)