n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')
visited = [False] * n

def dfs(start, now, cnt, cost):
    global answer

    if cost >= answer:
        return

    if cnt == n:
        if w[now][start] != 0:
            answer = min(answer, cost + w[now][start])
        return

    for nxt in range(n):
        if not visited[nxt] and w[now][nxt] != 0:
            visited[nxt] = True
            dfs(start, nxt, cnt + 1, cost + w[now][nxt])
            visited[nxt] = False


for s in range(n):
    visited[s] = True
    dfs(s, s, 1, 0)
    visited[s] = False

print(answer)