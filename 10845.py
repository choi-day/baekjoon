import sys
n = int(input())
count = 0
li = []

while(count != n):
    command = sys.stdin.readline().strip()
    if(command.startswith('push')):
        m = []
        for i in command:
            if(i.isdigit()): m.append(i)
        m = ''.join(map(str, m))
        li.append(m)
    if(command == 'pop'):
        if(len(li) == 0): print(-1)
        else:
            print(li.pop(0))
    if(command == 'size'):
        print(len(li))
    if(command == 'empty'):
        if(len(li) == 0): print(1)
        else:print(0)
    if(command == 'front'):
        if(len(li)==0): print(-1)
        else: print(li[0])
    if(command == 'back'):
        if(len(li) == 0):print(-1)
        else: print(li[len(li)-1])
    count = count + 1