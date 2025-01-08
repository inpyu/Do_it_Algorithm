num = int(input())
graph = [[]for _ in range(num)]
visited = [False] * num
D = [0] * num
lcm = 1

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

for i in range(num-1):
    a,b,p,q = map(int,input().split())
    graph[a].append((b,p,q))
    graph[b].append((a,q,p))
    lcm *= ((p * q) // gcd(p,q))

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1]
            dfs(next)

D[0] = lcm
dfs(0)
mgcd = D[0]

for i in range(1, num):
    mgcd = gcd(mgcd, D[i])
for i in range(num):
    print(int(D[i]//mgcd), end = " ")
