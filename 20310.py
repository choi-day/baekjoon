s = list(input())
zero = int(s.count('0')//2)
one = int(s.count('1')//2)

while(one != 0):
    s.remove('1')
    one -= 1

s = list(reversed(s))

while(zero != 0):
    s.remove('0')
    zero -=1
print(''.join(list(reversed(s))))