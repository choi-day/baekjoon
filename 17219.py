import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))
dict = {}

for _ in range(n):
    url, pw = sys.stdin.readline().strip().split(' ')
    dict[url] = pw
for _ in range(m):
    url = sys.stdin.readline().strip()
    print(dict[url])