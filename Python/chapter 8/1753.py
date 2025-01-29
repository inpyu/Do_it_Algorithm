import sys
input = sys.stdin.readline
from queue import PriorityQueue

node, edge = map(int, input().split())
start = int(input())
distance = [sys.maxsize] * (node +1)
visited = [False] * (node + 1)
graph = [[]for _ in range(node +1)]
q = PriorityQueue()

for _ in range(edge):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

q.put((0,start))
distance[start] = 0

while q.qsize()> 0 :
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in graph[c_v]:
        next = tmp[0]
        value = tmp[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))

for i in range(1, node+1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
