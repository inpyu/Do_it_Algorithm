import sys
input = sys.stdin.readline

n = int(input())
D = [[0 for _ in range(11) ] for _ in range(n+1)]

for i in range(1,10):
    D[1][i] = 1

for i in range(2, n+1):
    D[i][0] = D[i-1][1]
    D[i][9] = D[i-1][8]
    for j in range(1,9):
        D[i][j] = (D[i-1][j-1] + D[i-1][j+1])


sum = 0
for i in range(10):
    sum = sum + D[n][i]

print(sum % 1000000000)
