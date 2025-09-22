import sys

input = sys.stdin.readline

n = int(input())
colors = [list(input().strip()) for _ in range(n)]

from collections import deque

dirx = [1,-1,0,0]
diry = [0,0,1,-1]

def bfs(x,y, visited, colors):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dirx[i] 
            ny = y + diry[i]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                if colors[nx][ny] == colors[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = True

# 일반
cnt1 = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j, visited, colors)
            cnt1 += 1

# 색약
rg_colors = [[c if c != 'R' else 'G' for c in row] for row in colors]

cnt2 = 0
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if rg_colors[i][j] == 'R':
            rg_colors[i][j] = 'G'

        if not visited[i][j]:
            bfs(i,j, visited, rg_colors)
            cnt2 += 1

print(cnt1, cnt2)