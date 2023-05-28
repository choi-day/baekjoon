L = int(input())
word = input()
hashed = 0
for i, j in zip(word, range(L)):
    hashed = hashed + (ord(i)-96) * 31**j
print(hashed % 1234567891)