import sys
sys.setrecursionlimit(10**7)

def solution(n, lighthouse):
    graph = [[] for _ in range(n + 1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    dp = [[0, 0] for _ in range(n + 1)]

    def dfs(u):
        visited[u] = True
        dp[u][0] = 0   # u를 끄는 경우
        dp[u][1] = 1   # u를 켜는 경우

        for v in graph[u]:
            if not visited[v]:
                dfs(v)
                dp[u][0] += dp[v][1]
                dp[u][1] += min(dp[v][0], dp[v][1])

    dfs(1)
    return min(dp[1][0], dp[1][1])
