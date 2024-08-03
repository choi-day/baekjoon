import sys
input = sys.stdin.readline

code = input().strip()
n = int(input())
d = []
k = 0

for _ in range(n):
    d.append(input().strip())

while(k < 30):
    word = []
    for i in code:
        if ord(i) + k > 122:
            word.append(chr(ord(i)+k-26))
        else:
            word.append(chr(ord(i)+k))
    word = ''.join(word)
    for j in d:
        if j in word:
            print(word)
            k = 100
            break
    k+=1