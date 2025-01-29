import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
edges = []
distance = [sys.maxsize] * (node+1)

for _ in range(edge):
    start, end, time = map(int, input().split())
    edges.append((start,end,time))

distance[1] = 0

for _ in range(node-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time
        
cycle = False

for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        cycle = True

if not cycle:
    for i in range(2, node+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)