import sys

input = sys.stdin.readline

edge, vertex = map(int, input().split())
graph = {key : x for key, x in dict.fromkeys(range(1, edge+1)).items()}

for i in graph.keys():
    graph[i] = []

for _ in range(vertex):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = []
needVisited = []

def dfs(graph, start):
    global visited, needVisited

    needVisited.append(start)
    
    while needVisited:
        node = needVisited.pop()

        if(node not in visited):
            visited.append(node)
            needVisited.extend(graph[node])

count = 0
for i in graph.keys():
    if(i not in visited):
        dfs(graph, i)
        count += 1
print(count)