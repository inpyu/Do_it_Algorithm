from collections import deque

n = int(input())
graph = [[]for _ in range(n+1)]
indegree = [0] * (n+1)
time = [0] *(n+1)
result = [0] * (n+1)


for i in range(1,n+1):
    r = list(map(int, input().split()))
    time[i] = r[0]
    index = 1
    while True:
        temp = r[index]
        if temp == -1:
            break
        index += 1
        graph[temp].append(i)
        indegree[i] += 1

dq = deque()

for i in range(1,n+1):
    if indegree[i] == 0:
        dq.append(i)
while dq:
    now = dq.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        result[i] = max(result[i], result[now] + time[now])
        if indegree[i] == 0:
            dq.append(i)

for i in range(1, n+1):
    print(result[i] + time[i])