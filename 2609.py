n, m = map(int, input().split())

for i in (n, 2):
    if (n % i == 0):
        if(m % i == 0):
            GCD = i

print(GCD)

i = 1
while True :
    
    if(n*i == m*i):
        LMC = n*i
        print(LMC)
        break
    else:
        i += 1