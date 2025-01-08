import sys
import heapq
input = sys.stdin.readline

node, num, k = map(int, input().split())
graph = [[]for _ in range(node+1)]
distance = [[sys.maxsize] * k for _ in range(node+1)]

for _ in range(num):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

pq = [(0,1)] #1번 도시부터 출발
distance[1][0] = 0

while pq:
    cost, current_node  = heapq.heappop(pq)
    for nNode, nCost in graph[current_node ]:
        sCost = cost + nCost
        if distance[nNode][k-1] > sCost:
            distance[nNode][k-1] = sCost
            distance[nNode].sort()
            heapq.heappush(pq, [sCost, nNode])

for i in range(1, node+1):
    if distance[i][k-1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k-1])