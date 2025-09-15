n = int(input())
apt = [list(map(int, input().strip())) for _ in range(n)]

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque([(x,y)])
    apt[x][y] = 0
    cnt = 1
    while q: 
        x,y = q.popleft()
        for dir in range(4):
            nx = dx[dir] + x
            ny = dy[dir] + y
            if 0<=nx<n and 0<=ny<n and apt[nx][ny] == 1:
                q.append((nx,ny))
                apt[nx][ny] = 0
                cnt += 1
    return cnt


res = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            res.append(bfs(i,j))

print(len(res))
for r in sorted(res):
    print(r)