a, b, v = list(map(int, input().split(' ')))
count = int((v - a) / (a - b))
if((v - a) % (a - b) != 0): print(count+2)
else: print(count+1)