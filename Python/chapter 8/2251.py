from collections import deque

Sender = [0,0,1,1,2,2]
Reciever = [1,2,0,2,0,1]

now = list(map(int,input().split()))
visited = [[False for _ in range(201)] for _ in range(201)]
answer = [False] * 201

def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    answer[now[2]] = True

    while queue:
        now_node = queue.popleft()
        A = now_node[0]
        B = now_node[1]
        C = now[2] - A - B
        for k in range(6):
            next = [A,B,C]
            next[Reciever[k]] += next[Sender[k]]
            next[Sender[k]] = 0
            if next[Reciever[k]] > now[Reciever[k]]:
                next[Sender[k]] = next[Reciever[k]] - now[Reciever[k]]
                next[Reciever[k]] = now[Reciever[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0],next[1]))
                if next[0] == 0:
                    answer[next[2]] = True

bfs()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')