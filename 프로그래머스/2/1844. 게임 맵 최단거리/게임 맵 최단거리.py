from collections import deque

def solution(maps):
    
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    que = deque()
    que.append((0,0))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while que:
        cx,cy = que.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0<=nx<n and 0<=ny<m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[cx][cy] + 1
                que.append((nx,ny))
        
    answer = maps[n-1][m-1]
    
    if answer == 1:
        answer = -1
                                                    
    
    return answer