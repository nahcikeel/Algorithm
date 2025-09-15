from collections import deque

t = int(input())
for _ in range(t):
    n,m,v = map(int, input().split())

    farm = [[0]*m for _ in range(n)]
    for _ in range(v):
        r,c = map(int, input().split())
        farm[r][c] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    def bfs(x,y,farm,n,m):
        q = deque([(x,y)])
        farm[x][y] = 0
        while q:
            x,y = q.popleft()
            farm[x][y] = 0
            for dir in range(4):
                nx = dx[dir] + x
                ny = dy[dir] + y
                if 0<=nx<n and 0<=ny<m and farm[nx][ny] == 1:
                    farm[nx][ny] = 0
                    q.append((nx,ny))

    cnt = 0
    for i in range(m):
        for j in range(n):
            if farm[j][i] == 1:
                bfs(j, i, farm, n, m)
                cnt += 1
    print(cnt)