n = int(input())
sangLi = [0 for i in range(20000001)]
li = list(map(int, input().split(' ')))

for i in li:
    sangLi[i + 10000000] = sangLi[i + 10000000] + 1

m = int(input())
li = list(map(int, input().split(' ')))

for i in li:
    print(sangLi[i + 10000000], end=' ')