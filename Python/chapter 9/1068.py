import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n)]
visited = [False] * n
answer = 0

numList = list(map(int, input().split()))
deletedNode = int(input())
for i in range(n):
    if numList[i] == -1:
        root = i
    else:
        tree[i].append(numList[i])
        tree[numList[i]].append(i)

def dfs(v):
    visited[v] = True
    cNode = 0
    global answer
    for i in tree[v]:
        if not visited[i] and i != deletedNode:
            cNode += 1
            dfs(i)
    
    if cNode == 0:
        answer += 1


if deletedNode == root:
    print(0)
else:
    dfs(root)
    print(answer)