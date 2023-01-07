a = input()
list_a = []

for i in a:
    list_a.append(i)
for i in range(97, 123):
    if (chr(i) in list_a):
        print(list_a.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')
