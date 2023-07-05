n = int(input())
ver = int(input())

class Node:
    def __init__(self,e):
        self.e = e
        self.next = None

edge = [Node(0) for i in range(n+1)]

for i in range(1, n+1):
    edge[i] = Node(i)

for i in range(ver):
    e, v = map(int, input().split(' '))
    node = edge[e]
    while node.next:
        node = node.next
    node.next = Node(v)
    node = edge[v]
    while node.next:
        node = node.next
    node.next = Node(e)

virus = []
virus.append(1)
deep = []

def dfs(li, f):
    head = li[f]
    while head.next:
        k = head.next
        head = k
        if(k.e not in virus): virus.append(k.e); dfs(li, k.e)

dfs(edge, 1)
print(len(virus)-1)