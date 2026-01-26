n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

for i in range(1,n):
    for j in range(m):
        if (j-1 >=0) and (j+1 < m):
            dp[i][j] = graph[i][j] + max(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

INF = 10**9
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]

for j in range(m):
    for d in range(3):
        dp[0][j][d] = graph[0][j]
        
 
for i in range(1,n):
    for j in range(m):

        if j-1>=0:
            dp[i][j][0] = graph[i][j] + min(dp[i-1][j-1][1], dp[i-1][j-1][2])

        dp[i][j][1] = graph[i][j] + min(dp[i-1][j][0], dp[i-1][j][2]) 

        if j+1 < m:
            dp[i][j][2] = graph[i][j] + min(dp[i-1][j+1][0], dp[i-1][j+1][1])

answer = min(min(dp[n-1][j]) for j in range(m))
print(answer)