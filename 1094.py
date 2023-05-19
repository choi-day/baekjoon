X = int(input())
count = 0

for i in range(6,-1,-1):
    if(X - 2**i < 0 ): pass
    elif( X - 2**i == 0): print(count+1); break
    else: X = X - 2**i; count = count+1