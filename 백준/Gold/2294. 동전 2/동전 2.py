n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

INF = 10**9
dp = [INF] * (k + 1)
dp[0] = 0

for c in coins:
    for x in range(c, k+1):
        dp[x] = min(dp[x], dp[x-c]+1)


print(dp[k] if dp[k] < INF else -1)