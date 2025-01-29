import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [-1] * (n + 1)
visited[x] = 0

def dfs(v):
    for next_node in graph[v]:
        if visited[next_node] == -1 or visited[next_node] > visited[v] + 1:
            visited[next_node] = visited[v] + 1
            dfs(next_node)

dfs(x)

found = False
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
