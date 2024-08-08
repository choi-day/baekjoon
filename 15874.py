k, lenS = map(int, input().split())
s = input()
c = []

for i in s:
    a = ord(i)
    if a >= ord('a') and a <= ord('z'):
        if a+(k%26)> ord('z'):
            print(chr(a+(k%26)-26), end = '')
        else:
            print(chr(a+(k%26)), end = '')
    elif a >= ord('A') and a <= ord('Z'):
        if a+(k%26) > ord('Z'):
            print(chr(a+(k%26)-26), end = '')
        else:
            print(chr(a+(k%26)), end = '')
    else:
        print(i, end = '')