from collections import deque

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            target = (i,j)

q = deque()
q.append(target)

distance = [[-1] * m for _ in range(n)]
distance[target[0]][target[1]] = 0

dirs = [(-1,0), (1,0), (0,-1), (0,1)]


while q:
    x,y = q.popleft()

    for dx,dy in dirs:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and distance[nx][ny] == -1 and graph[nx][ny] == 1:
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=" ")
        else:
            print(distance[i][j], end=" ")
    print()
