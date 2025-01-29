from collections import deque

n = int(input())
graph = [[]for _ in range(n+1)]
visited = [False] * (n+1)
distance = [0] * (n+1)

for i in range(n):
    num_list = list(map(int,input().split()))
    for j in range(1,len(num_list),2):
        if num_list[j] == -1:
            break
        graph[num_list[0]].append((num_list[j],num_list[j+1]))

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if not visited[i[0]]:
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_node] + i[1]

bfs(1)
max = 1
for i in range(2, n+1):
    if distance[max] < distance[i]:
        max = i

visited = [False] * (n+1)
distance = [0] * (n+1)
bfs(max)
distance.sort()
print(distance[n])