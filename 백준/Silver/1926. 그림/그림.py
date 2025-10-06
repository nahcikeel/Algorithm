from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(i,j):
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    q = deque()
    q.append((i,j))
    graph[i][j] = 0
    area = 1

    while q:
        cx, cy = q.popleft()

        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                area += 1

    return area

cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            max_area = max(max_area, bfs(i,j))
            
print(cnt)
print(max_area)