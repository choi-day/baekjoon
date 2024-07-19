from collections import Counter

numList = []
for _ in range(10):
    numList.append(int(input()))

counter = Counter(numList)
mode = counter.most_common(1)
print(int(sum(numList) / 10))
print(mode[0][0])