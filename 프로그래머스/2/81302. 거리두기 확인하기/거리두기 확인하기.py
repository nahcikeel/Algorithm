from collections import deque


def bfs(place,x,y):
    q = deque()
    q.append((x,y,0))
    
    visited = [[False]*5 for _ in range(5)]
    visited[x][y] = True
    
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    while q:
        x,y,dist = q.popleft()
        
        if dist>=2:
            continue
        
        
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            
            if nx<0 or 5<=nx or 0>ny or 5<=ny:
                continue
            if place[nx][ny] == 'X':
                continue
            if visited[nx][ny]:
                continue
                
            if place[nx][ny] == 'P':
                return False
            
            visited[nx][ny] = True
            q.append((nx,ny,dist+1))

    return True

def solution(places):
    answer = []
    
    
    for place in places:
        ok = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    result = bfs(place,i,j)
                    if result == False:
                        ok = False
        answer.append(1 if ok else 0)
    
    return answer