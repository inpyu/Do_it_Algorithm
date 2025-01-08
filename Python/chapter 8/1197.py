import sys
from queue import PriorityQueue

input = sys.stdin.readline

node, edge = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (node+1)

for i in range(node+1):
    parent[i] = i

for _ in range(edge):
    start, end, cost = map(int, input().split())
    pq.put((cost, start, end))

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b= find(b)
    if a!=b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < node -1:
    cost, start, end = pq.get()
    if find(start) != find(end):
        union(start, end)
        result += cost
        useEdge += 1

print(result)
