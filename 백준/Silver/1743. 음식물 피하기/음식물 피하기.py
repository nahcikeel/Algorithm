from collections import deque

n,m,k = map(int, input().split())
graph = [[0] * (m+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1

visited = [[False] * m for _ in range(n)]
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = True
    cnt = 1

    while q:
        cx,cy = q.popleft()

        for dx,dy in dirs:
            nx,ny = cx+dx, cy+dy

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    cnt += 1
    return cnt


total = 0
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==False:
            result = bfs(i,j)
            total = max(result, total)

print(total)