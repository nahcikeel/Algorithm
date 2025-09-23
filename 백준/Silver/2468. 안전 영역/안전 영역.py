n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x, y, visited, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    while q:
        cx, cy = q.popleft()
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
                visited[nx][ny] = True
                q.append((nx, ny))

max_height = max(map(max, graph))
result = 0

for h in range(0, max_height+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]>h and visited[i][j]==False:
                bfs(i,j,visited,h)
                cnt += 1
    result = max(result, cnt)
    
print(result)