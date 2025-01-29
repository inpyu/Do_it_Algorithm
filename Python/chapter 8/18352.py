import sys
from collections import deque

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


queue = deque([x])
visited = [-1] * (n + 1)
visited[x] = 0

while queue:
    current = queue.popleft()
    for next_node in graph[current]:
        if visited[next_node] == -1:
            visited[next_node] = visited[current] + 1
            queue.append(next_node)

found = False
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
