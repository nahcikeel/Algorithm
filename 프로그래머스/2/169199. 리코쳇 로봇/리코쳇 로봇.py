from collections import deque

def bfs(red,green,board):
    
    q = deque()
    q.append((red[0],red[1],0))
    
    visited = [[False]*m for _ in range(n)]
    visited[red[0]][red[1]] = True
    
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while q:
        x,y,cnt = q.popleft()
        
        if (x,y) == green:
            return cnt
        
        for dx,dy in dirs:
            nx,ny = x,y
            
            while True:
                tx,ty = nx+dx, ny+dy
                
                if not (0<=tx<n and 0<=ty<m):
                    break
                if board[tx][ty] == 'D':
                    break
                    
                nx,ny = tx,ty
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    
    return -1

def solution(board):
    answer = 0
    
    global n,m
    n,m = len(board), len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                red = (i,j)
            elif board[i][j] == 'G':
                green = (i,j)
    
    return bfs(red,green,board)