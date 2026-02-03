from collections import deque

def bfs(start, maps, visited):
    day = int(maps[start[0]][start[1]])
    q = deque([start])
    visited[start[0]][start[1]] = True
    
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while q:
        x,y = q.popleft()
        
        for dx,dy in dirs:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny]!='X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    day += int(maps[nx][ny])
                    q.append((nx,ny))

    
    return day

def solution(maps):
    
    global n,m
    n =len(maps)
    m = len(maps[0])

    visited = [[False]*m for _ in range(n)]
    answer = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]!='X' and not visited[i][j]:
                answer.append(bfs((i,j),maps, visited))
                
    if not answer:
        return [-1]
    
    return sorted(answer)