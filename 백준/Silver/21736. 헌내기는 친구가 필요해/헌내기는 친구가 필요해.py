n,m = map(int , input().split())
campus = [list(input()) for _ in range(n)]

from collections import deque

dirs = [(0,1), (0,-1), (1,0), (-1,0)]
visited = [[False]*(m+1) for _ in range(n)]

def bfs(x,y):
    result = 0
    q = deque([(x,y)])
    visited[x][y] = True

    while q:
        cur_x, cur_y = q.popleft()

        for dx, dy in dirs:
            nx = cur_x + dx
            ny = cur_y + dy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and campus[nx][ny] != 'X':
                if campus[nx][ny] == 'P':
                    result += 1
                    q.append((nx,ny))
                    visited[nx][ny] = True
                elif  campus[nx][ny] == 'O':
                    q.append((nx,ny))
                    visited[nx][ny] = True

    return result

for i in range(n):
    for j in range(m):
        if campus[i][j] == 'I':
            x,y = i,j
            break

result = bfs(x,y)

if result == 0:
    print('TT')
else:
    print(result)