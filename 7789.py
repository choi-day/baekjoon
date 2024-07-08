n , new = input().split()
isNMino = True
isNewMino = True
newN = int(new+n)
n = int(n)

for i in range(2, int(n**0.5+1)):
    if n % i == 0:
        isNMino = False
        break
for i in range(2, int(newN**0.5+1)):
    if newN % i == 0:
        isNewMino = False
        break
if isNMino and isNewMino:
    print('Yes')
else:
    print('No')