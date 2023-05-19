N = int(input())
word = []

for i in range(N):
    i = input()
    word.append(i)

word = list(set(word))

word.sort()
word.sort(key = len)

for i in word:
    print(i)