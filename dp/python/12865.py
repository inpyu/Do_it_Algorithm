import sys

input = sys.stdin.readline

n, k = map(int, input().split())
weight = [0] * (n+1)
value = [0] * (n+1)

for i in range(1,n+1):
    weight[i], value[i] = map(int, input().split())

DP = [[0] * (k+1) for _ in range(n+1)]
for current in range(1,n+1):
    for limit in range(1, k+1):
        if weight[current] <= limit :
            DP[current][limit] = max(DP[current-1][limit], DP[current-1][limit-weight[current]] + value[current])
        else:
            DP[current][limit] = DP[current-1][limit]

print(DP[-1][-1])