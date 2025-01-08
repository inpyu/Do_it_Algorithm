from collections import deque

node, edge, start = map(int,input().split())
graph = [[]for _ in range(node + 1)]
visited = [False] * (node + 1)

for i in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(node + 1):
    graph[i].sort()

def DFS(v):
    print(v, end=" ")
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

DFS(start)

visited = [False] * (node + 1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        print(now_node, end = " ")
        for i in graph[now_node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

print()
BFS(start)