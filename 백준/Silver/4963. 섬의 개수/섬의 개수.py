import sys
input = sys.stdin.readline

from collections import deque

def bfs(x,y, visited, islands):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()
        for i in range(8):
            nx, ny = cx + dirs[i][0], cy + dirs[i][1]
            if 0<=nx<h and 0<=ny<w and visited[nx][ny] == False and islands[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))

while True:
    w,h = map(int, input().split())
    if w==0 and h==0:
        break
    islands = [list(map(int, input().split())) for _ in range(h)]

    dirs = [(1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)]

    cnt = 0
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if islands[i][j] == 1 and visited[i][j] == False:
                bfs(i,j,visited,islands)
                cnt += 1

    print(cnt)