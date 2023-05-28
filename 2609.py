n, m = sorted(list(map(int, input().split())))
for i in range(n, 0, -1):
    if ((n % i == 0) &(m % i == 0)):
        GCD = i
        break
    else: pass
print(GCD)

LCM = int(GCD * (n/GCD) * (m/GCD))
print(LCM)