import math
import cmath

x = int(input())
c = cmath.sqrt(1-(4*x*2))/1j
n = math.ceil((c.real-1)/2)

if(n%2==0):
    a =  n - (n*(n+1)/2 - x)
    b = (n*(n+1)/2 - x) + 1

else:
    a = (n*(n+1)/2 - x) + 1
    b = n - (n*(n+1)/2 - x)

print(int(a) , "/", int(b), sep = '')