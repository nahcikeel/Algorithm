from collections import deque
import sys

input = sys.stdin.readline


m,n,h = map(int, input().split())
boxes = [ [ list(map(int, input().split())) for _ in range(n) ] for _ in range(h) ]

q = deque()

for z in range(h):
    for y in range(n):
        for x in range(m): 
            if boxes[z][y][x] == 1:
                q.append((z,y,x))
dirs = [(1,0,0), (-1,0,0), (0,1,0),
        (0,-1,0), (0,0,1), (0,0,-1)]

while q:
    z,y,x, = q.popleft()
    for dz,dy,dx in dirs:
        nz, ny, nx = z+dz, y+dy, x+dx
        if 0<=nz<h and 0<=ny<n and 0<=nx<m and boxes[nz][ny][nx]==0:
            boxes[nz][ny][nx] = boxes[z][y][x] + 1
            q.append((nz,ny,nx))



ans = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if boxes[z][y][x] == 0:
                print(-1)
                sys.exit(0)
            ans = max(ans, boxes[z][y][x])
print(ans-1)