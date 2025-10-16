m,n,k = map(int, input().split())

graph = [[0]*n for _ in range(m)]

for _ in range(k):
    x1,y1, x2,y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

from collections import deque

visited = [[False]*n for _ in range(m)]
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(x,y):
    cnt = 1
    q = deque([(x,y)])
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy

            if 0<=nx<m and 0<=ny<n and visited[nx][ny]==False and graph[nx][ny]==0:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx,ny))
    return cnt

answer = []

for i in range(m):
    for j in range(n):
        if graph[i][j]==0 and visited[i][j] == False:
            result = bfs(i,j)
            answer.append(result)
answer.sort()

print(len(answer))
print(*answer)