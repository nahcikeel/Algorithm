from collections import deque

def bfs(x,y, visited, n, m, land, idx_map, idx):
    
    cnt = 1
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    q = deque([(x,y)])
    visited[x][y] = True
    idx_map[x][y] = idx
    
    while q:
        cx,cy = q.popleft()
        for dx,dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and land[nx][ny] == 1:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx,ny))
                idx_map[nx][ny] = idx
                
    return cnt


def solution(land):
    
    n = len(land)
    m = len(land[0])
    sizes = []
    
    visited = [[False]*m for _ in range(n)]
    idx_map = [[0]*m for _ in range(n)]
    all_oils = []
    oil_size = {}  # {덩어리 ID: 크기}
    idx = 1
    
    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and not visited[i][j]:
                oil_size[idx] = bfs(i,j, visited, n, m, land, idx_map, idx)
                idx += 1
                
    max_oil = 0
    for col in range(m):
        total = 0
        seen = set()
        for row in range(n):
            if idx_map[row][col] != 0:
                oil_id = idx_map[row][col]
                if oil_id not in seen:
                    seen.add(oil_id)
                    total += oil_size[oil_id]
        max_oil = max(max_oil, total)
            
              
    return max_oil