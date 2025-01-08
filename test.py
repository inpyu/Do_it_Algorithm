
A  = [2,1,0,1,2,9,1,0]
n = len(A)
dp = [0] * n
dp[0] = A[0]
    
for i in range(1, n):
    dp[i] = max(dp[i-1] + A[i], int(str(A[i-1]) + str(A[i])) + (dp[i-2] if i > 1 else 0))
    
print(dp[-1])