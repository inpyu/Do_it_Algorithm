import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(node + 1)]
visited = [False] * (node+1)

def DFS(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

for _ in range(edge):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0

for i in range(1,node+1):
    if not visited[i]:
        DFS(i)
        count +=1

print(count)

