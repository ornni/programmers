import sys

n = int(input())
mod = 1000000000
dp = [0] * 1000001

dp[2] = 1

for i in range(3, n+1):
    dp[i] = (i-1) * (dp[i-1] + dp[i-2]) % mod

print(dp[n])