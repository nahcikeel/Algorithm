from collections import deque
import sys

input = sys.stdin.readline

n,l,r = map(int, input().split())
kingdom = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    union = [(x,y)]
    total = kingdom[x][y]

    while q:
        cx,cy = q.popleft()

        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(kingdom[cx][cy] - kingdom[nx][ny]) <= r:
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total += kingdom[nx][ny]

    return union, total

day = 0
while True:
    visited = [[False]*n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total = bfs(i,j,visited)
                if len(union) > 1:
                    moved = True
                    new_pop = total // len(union)
                    for x,y in union:
                        kingdom[x][y] = new_pop

    if not moved:
        break
    day += 1

print(day)