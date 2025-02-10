num, count = map(int, input().split())
coin = []
for i in range(num):
    coin.append(int(input()))

dp = [100001] * (count+1)
dp[0] = 0

for c in coin:
    for j in range(c, count + 1):
        if dp[j] > 0:
            dp[j] = min(dp[j], dp[j-c] + 1)
        
if dp[count] == 10001:
    print(-1)
else:
    print(dp[count])