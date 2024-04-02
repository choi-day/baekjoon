l = int(input())

s = sorted(list(map(int, input().split())))
n = int(input())

if (n in s) or (n > s[len(s)-1] or n < s[0]):
    print(0)
else:
    for i in range(len(s)):
        if (s[i] < n) and (n < s[i+1]):
            k = i
            break
    print((n - s[k]) * (s[k+1] - n)-1)