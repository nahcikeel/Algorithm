from collections import deque

n, m = map(int, input().split())
war = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(y, x, team):
    q = deque([(y, x)])
    visited[y][x] = True
    cnt = 1

    while q:
        cy, cx = q.popleft()

        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx

            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx] and war[ny][nx] == team:
                visited[ny][nx] = True
                q.append((ny, nx))
                cnt += 1

    return cnt

white = 0
blue = 0

for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            if war[y][x] == 'W':
                white += bfs(y, x, 'W') ** 2
            else:
                blue += bfs(y, x, 'B') ** 2

print(white, blue)
