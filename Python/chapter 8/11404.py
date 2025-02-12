import sys
input = sys.stdin.readline

n = int(input())
count = int(input())
graph = [[sys.maxsize for _ in range(n+1) ] for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(count):
    s, e, cost = map(int, input().split())
    if graph[s][e] > cost:
        graph[s][e] = cost

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()