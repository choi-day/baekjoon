t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    plain = input()
    cipher = []
    for j in plain:
        cipher.append(chr((a * (ord(j)-65) + b)  % 26 + 65))
    print(''.join(cipher))