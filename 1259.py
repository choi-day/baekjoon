a = 'a'
while(a != '0'):
    a = input()
    if(a == '0'): pass
    elif(a == a[::-1]): print('yes')
    else: print('no')