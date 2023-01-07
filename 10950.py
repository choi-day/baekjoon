n = int(input())
num_array = list()

for i in range(0, n) :
    n1, n2 = map(int, input().split())
    num_array.append(n1+n2)

for i in num_array :
    print(i)