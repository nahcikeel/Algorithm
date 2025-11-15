from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

INF = 10**9
dist = [[INF]*m for _ in range(n)]
dist[0][0] = 0

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
q = deque([(0,0)])

while q:
    cx, cy = q.popleft()
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < n and 0 <= ny < m:
            cost = 1 if maze[nx][ny] == 1 else 0
            if dist[nx][ny] > dist[cx][cy] + cost:
                dist[nx][ny] = dist[cx][cy] + cost
                if cost == 1:
                    q.append((nx, ny))
                else:
                    q.appendleft((nx, ny))

print(dist[n-1][m-1])
