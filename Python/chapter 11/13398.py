n = int(input())
num_list = list(map(int, input().split()))

L = [0] * n
L[0] = num_list[0]
result = L[0]

for i in range(1,n):
    L[i] = max(num_list[i],L[i-1] + num_list[i])
    result = max(result, L[i])

R = [0] * n
R[n-1] = num_list[n-1]

for i in range(n-2, -1, -1):
    R[i] = max(num_list[i], R[i+1] + num_list[i])

for i in range(1, n-1):
    temp = L[i-1] + R[i+1]
    result = max(result, temp)

print(result)