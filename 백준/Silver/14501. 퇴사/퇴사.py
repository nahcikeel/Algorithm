n = int(input())

schedules = []
dp = [0]*(n+2)

for _ in range(n):
    schedules.append(list(map(int, input().split())))

for i in range(n,0,-1):
    day,pay = schedules[i-1]
    if i+day <= n+1:
        dp[i] = max(dp[i+1], pay+dp[i+day])
    else:
        dp[i] = dp[i+1]

print(dp[1])