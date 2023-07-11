import sys
equation = sys.stdin.readline()
num = []
sign = []
n = []
for i in equation:
    if(i.isdigit()):
        n.append(i)
    else:
        sign.append(i)
        k = ''.join(n)
        num.append(int(k))
        n = []
sign_copy = sign[:]

for i in sign:
    if( i == '+'):
        k = sign_copy.index('+')
        sign_copy.pop(sign_copy.index('+'))
        a = num.pop(k)
        b = num[k]
        num[k] = a + b
if(len(num) != 1 ):
    result = num[0]
    for i in num:
        result -= i
    print(result + num[0])
else: print(*num)