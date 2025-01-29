import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
visited = [False] * (node+1)

for _ in range(edge):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

arrive = False

def DFS(v, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[v] = False


for i in range(node):
    DFS(i, 1)
    if arrive:
        break
if arrive:
    print(1)
else:
    print(0)