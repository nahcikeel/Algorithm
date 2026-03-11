from collections import deque

def solution(board):
    n = len(board)
    
    INF = float('inf')
    cost = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    
    dirs = [(0,-1), (0,1), (1,0), (-1,0)]
    # nc = 0
    
    q = deque()
    for i in range(4):
        cost[0][0][i] = 0
        q.append((0,0,i,0))
    
    while q:
        x,y,d,c = q.popleft()
        for nd in range(4):
            nx, ny = x + dirs[nd][0], y + dirs[nd][1]
            
            if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1:
                
                if d == nd:
                    nc = c + 100
                else:
                    nc = c + 600
            
                if cost[nx][ny][nd] > nc:
                    cost[nx][ny][nd] = nc
                    q.append((nx,ny,nd,nc))
    
    return min(cost[n-1][n-1])