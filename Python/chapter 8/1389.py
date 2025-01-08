import sys
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0

for _ in range(e):
    N, M = map(int, input().split())
    graph[N][M] = 1
    graph[M][N] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

Min = sys.maxsize
answer = -1

for i in range(1, n+1):
    temp = 0
    for j in range(1, n+1):
        temp += graph[i][j]
    if Min > temp:
        Min = temp
        answer = i

print(answer)