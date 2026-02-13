n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def dfs(x, y, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return
    
    for dx,dy in dirs:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny, depth+1, total+graph[nx][ny])
            visited[nx][ny] = False

    return

def check_t(x,y):
    global answer
    center = graph[x][y]
    wings = []

    for dx,dy in dirs:
        nx,ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            wings.append(graph[nx][ny])

    if len(wings) >= 3:
        total = center + sum(wings)
        if len(wings) == 4:
            total -= min(wings)
        answer = max(answer, total)

    return


visited = [[False]*m for _ in range(n)]
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
answer = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j, 1, graph[i][j])
        visited[i][j] = False

        check_t(i,j)

print(answer)