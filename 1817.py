n , m = map(int, input().split())

if n == 0:
    print(0)
else:
    a = list(map(int, input().split()))
    count = 1
    k = m
    for i in range(0, n):
        if k >= a[i]:
            k -= a[i]
        else:
            count += 1
            k = m 
            k -= a[i]
    print(count)