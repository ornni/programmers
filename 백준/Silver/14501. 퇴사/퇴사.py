import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+2)
time = [0] * (n+1)
price = [0] * (n+1)

for i in range(1, n+1):
    time[i], price[i] = map(int, input().split())

for i in range(n, 0, -1):
    if time[i] + i > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], price[i] + dp[i + time[i]])

print(dp[1])