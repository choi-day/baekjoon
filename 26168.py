import bisect
import sys
input = sys.stdin.readline
print = sys.stdout.write
def more_then(li, x):
    return len(li) - bisect.bisect_right(li, x-1)

def more(li, x):
    return len(li) - bisect.bisect_right(li, x)

def between(li, x, y):
    return bisect.bisect_right(li, y) - bisect.bisect_left(li, x)
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
for i in range(m):
    option, *t = map(int, input().split())
    if option == 1:
        print(str(more_then(lst, *t)) + "\n")
    
    elif option == 2:
        print(str(more(lst, *t)) + "\n")
    
    else:
        print(str(between(lst, *t)) + "\n")