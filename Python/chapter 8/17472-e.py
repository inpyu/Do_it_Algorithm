import copy
import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

# 네 방향 (오른쪽, 아래, 왼쪽, 위)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
myMap = []
for i in range(N):
    myMap.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
islands = []
sNum = 0

# 섬의 구역 번호 매기기
def BFS(i, j, sNum):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    myMap[i][j] = sNum
    island = [(i, j)]  # 섬의 좌표들 저장

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and myMap[nr][nc] == 1:
                visited[nr][nc] = True
                myMap[nr][nc] = sNum
                queue.append((nr, nc))
                island.append((nr, nc))
    
    islands.append(island)

# 섬 번호 매기기
for i in range(N):
    for j in range(M):
        if myMap[i][j] == 1 and not visited[i][j]:
            sNum += 1
            BFS(i, j, sNum)

# 가능한 다리 찾기
def find_bridges():
    pq = PriorityQueue()

    for island in islands:
        for r, c in island:
            for d in range(4):
                nr, nc = r, c
                length = 0

                # 해당 방향으로 계속 바다(0)일 때만 다리 놓기
                while True:
                    nr += dr[d]
                    nc += dc[d]
                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        break
                    if myMap[nr][nc] == myMap[r][c]:
                        break
                    if myMap[nr][nc] == 0:
                        length += 1
                    elif myMap[nr][nc] != myMap[r][c]:
                        if length >= 2:  # 다리 길이는 2 이상이어야 함
                            pq.put((length, myMap[r][c], myMap[nr][nc]))
                        break
    return pq

# 유니온 파인드
def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

# 다리 찾기
pq = find_bridges()

# 유니온 파인드 초기화
parent = [i for i in range(sNum + 1)]
useEdge = 0
result = 0

# 최소 스패닝 트리 구성
while not pq.empty():
    length, island1, island2 = pq.get()
    if find(island1) != find(island2):
        union(island1, island2)
        result += length
        useEdge += 1

# 모든 섬이 연결되었는지 확인 (사용한 엣지가 sNum-1개여야 함)
if useEdge == sNum - 1:
    print(result)
else:
    print(-1)
