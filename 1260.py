from collections import deque

def DFS(graph, root): #dfs 구현
    visited = [] #방문 된 것 넣어두는 용도
    stack = [root] #dfs실행 중 필요한 스택, 선입후출, 방문 해야 하는 곳, root부터 탐색을 시작하므로 root를 stack에 넣어둠

    while stack: #스택에 값이 있는 동안은
        n = stack.pop() #스택에서 가장 마지막 값(최근에 넣은 값) pop
        if n not in visited: #그 값이 방문되지 않았다면
            visited.append(n) #방문했으므로 visited에 추가
            if n in graph: #방문한 값이 graph에 있다면
                temp = list(set(graph[n]) - set(visited)) #temp는 n과 간선으로 연결된 집합에서 방문 된 집합의 차집합의 리스트
                temp.sort(reverse=True) #temp를 내림차순으로 정렬(문제에서 작은 값부터 출력 하라고 했으므로)
                stack += temp #stack에 temp추가
    return " ".join(str(i) for i in visited) #방문한 순서대로 visited에 넣어서 return

def BFS(graph, root): #bfs구현
    visited = []
    queue = deque([root]) #bfs는 queue를 사용함, 선입선출

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)

  
graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))