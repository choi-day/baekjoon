import sys
input = sys.stdin.readline

k, s, n = input().split()
n = int(n)

kcol = ord(list(k)[0])
krow = int(list(k)[1])

scol = ord(list(s)[0])
srow = int(list(s)[1])

for _ in range(n):
    command =  input().split()[0]
    if(command == 'R'):
        if(kcol + 1 > 72):
            continue
        elif(kcol+1 == scol and krow == srow):
            if(scol + 1 > 72):
                continue
            else: kcol += 1; scol += 1
        else: kcol += 1
    elif(command == 'L'):
        if(kcol - 1 < 65):
            continue
        elif(kcol -1 == scol and krow == srow):
            if(scol -1 < 65):
                continue
            else: kcol -= 1; scol -=1
        else: kcol -= 1
    elif(command == 'B'):
        if(krow - 1 < 1):
            continue
        elif(kcol == scol and krow-1 == srow):
            if(srow - 1 < 1):
                continue
            else: krow -= 1; srow -= 1
        else: krow -= 1
    elif(command == 'T'):
        if(krow + 1 > 8):
            continue
        elif(kcol == scol and krow+1 == srow):
            if(srow + 1 > 8):
                continue
            else: srow += 1; krow+=1
        else: krow += 1
    elif(command == 'RT'):
        if(krow + 1 > 8 or kcol + 1 > 72):
            continue
        elif(kcol+1 == scol and krow+1 == srow):
            if(srow + 1 > 8 or scol +1 > 72):
                continue
            else: srow += 1; scol +=1; kcol +=1; krow+=1
        else: krow += 1; kcol+=1
    elif(command == 'LT'):
        if(krow + 1 > 8 or kcol - 1 < 65):
            continue
        elif(kcol-1 == scol and krow+1 == srow):
            if(srow + 1 > 8 or scol - 1 < 65):
                continue
            else: srow += 1; scol -=1; kcol -=1; krow+=1
        else: krow += 1; kcol-=1
    elif(command == 'RB'):
        if(krow - 1 < 1 or kcol + 1 > 72):
            continue
        elif(kcol+1 == scol and krow-1 == srow):
            if(srow - 1 < 1 or scol +1 > 72):
                continue
            else: srow -= 1; scol +=1; kcol +=1; krow-=1
        else: krow -= 1; kcol+=1
    elif(command == 'LB'):
        if(krow - 1 < 1 or kcol - 1 < 65):
            continue
        elif(kcol-1 == scol and krow-1 == srow):
            if(srow - 1 < 1 or scol - 1 < 65):
                continue
            else: srow -= 1; scol -=1; kcol -=1; krow-=1
        else: krow -= 1; kcol-=1

print(chr(kcol),krow, sep='')
print(chr(scol),srow, sep='')