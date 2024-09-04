import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

test_num = int(input())

def dfs(v):
    global isEven
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            check[i] = (check[v]+1)%2
            dfs(i)
        elif check[v] == check[i]:
            isEven = False

for i in range(test_num):
    node, edge = map(int, input().split())
    graph = [[]for _ in range(node +1)]
    visited = [False] * (node+1)
    check = [0] * (node +1)
    isEven = True
    for j in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, node +1):
        if isEven:
            dfs(i)
        else:
            break
    if isEven:
        print("YES")
    else:
        print("NO")