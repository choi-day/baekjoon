n = int(input())
count = 0
while(count != n):
    a = input()
    li = []
    for i in a:
        if(i == '('):
            li.append(i)
        if(i == ')'):
            if(len(li) == 0): li.append(i)
            else:  
                j = li.pop(len(li)-1)
                if(j == '('): pass
                else: li.append(j)
    if(len(li)==0): print('YES')
    else: print('NO')
    count = count+1