import sys
n = int(input())
li = []
count = 0
while(count !=n ):
    command = sys.stdin.readline().strip()
    if(command == 'pop'):
        if(len(li) == 0): print(-1)
        else: print(li.pop(len(li)-1))
    if(command == 'size'):
        print(len(li))
    if(command == 'empty'):
        if(len(li) == 0): print(1)
        else: print(0)
    if(command == 'top'):
        if(len(li) == 0): print(-1)
        else: print(li[len(li)-1])
    if(command.startswith('push')):
        m = []
        for i in command:
            if(i.isdigit()): m.append(i)
        m = ''.join(map(str, m))
        li.append(int(m))
    count = count + 1