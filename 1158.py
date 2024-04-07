n, k = map(int, input().split())
li = [i for i in range(1, n+1)]
print('<', end='')

i = k-1

print(li[i], end=',')
li.remove(li[i])

for t in range(n-2):
    i += (k-1)
    if i >= len(li):
        i = i % len(li)
    a =  li[i]
    li.remove(a)
    print('', a, end=',')
print('', str(li[0]) + '>')
