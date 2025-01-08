import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
visited = [False] * (N+1)
tree = [[]for _ in range(N+1)]
answer = [0] * (N+1)

for _ in range(N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(v):
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            answer[i] = v
            visited[i] = True
            dfs(i)

dfs(1)
for i in range(2, N+1):
    print(answer[i])