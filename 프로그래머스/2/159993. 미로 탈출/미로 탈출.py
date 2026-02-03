from collections import deque

def bfs(start, target, maps):
    
    q = deque()
    q.append(start)
    visited = [[-1]*m for _ in range(n)]
    visited[start[0]][start[1]] = 0
    
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while q:
        x,y = q.popleft()
        if maps[x][y] == target:
            return visited[x][y]
        
        for dx,dy in dirs:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    
    return -1

def solution(maps):
    
    global n,m
    n = len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                start = [i,j]
            elif maps[i][j]=='L':
                lever = [i,j]
    
    d1 = bfs(start, 'L', maps)
    d2 = bfs(lever, 'E', maps)
    
    if d1==-1:
        return -1
    if d2==-1:
        return -1
    
    return d1+d2