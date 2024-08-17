m = list(input())

happy = 0
sad = 0

for i in range(2, len(m)):
    if m[i] == ')':
        if m[i-1] == '-' and m[i-2] == ':':
            happy += 1
    elif m[i] == '(':
        if m[i-1] == '-' and m[i-2] == ':':
            sad += 1

if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')