from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])

    grid = [['.']*(m+2)]
    for row in storage:
        grid.append(['.'] + list(row) + ['.'])
    grid.append(['.']*(m+2))
    
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def remove_forklift(c):
        can_reach = set()
        visited = [[False]*(m+2) for _ in range(n+2)]
        q = deque()
        q.append((0,0))
        visited[0][0] = True
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n+2 and 0 <= ny < m+2 and not visited[nx][ny]:
                    if grid[nx][ny] == c:
                        can_reach.add((nx, ny))

                    elif grid[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx, ny))

        for rx, ry in can_reach:
            grid[rx][ry] = '.'

    def remove_crane(c):
        for i in range(1, n+1):
            for j in range(1, m+1):
                if grid[i][j] == c:
                    grid[i][j] = '.'

    for req in requests:
        c = req[0]
        if len(req) == 1:
            remove_forklift(c)
        else:
            remove_crane(c)

    remaining = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if grid[i][j] != '.':
                remaining += 1
                
    return remaining