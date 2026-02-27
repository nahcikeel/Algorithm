c,n = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [INF] * (c+100)
dp[0] = 0

for cost, people in cities:
    for i in range(people, c+100):
        dp[i] = min(dp[i], dp[i-people] + cost)

print(min(dp[c:]))