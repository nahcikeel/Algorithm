import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]

from collections import deque

visited = [[[False] *2 for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0,0,0,1))
visited[0][0][0] = True
answer = -1

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

while q:
    cx, cy, broken, dis = q.popleft()

    if cx == n-1 and cy == m-1:
        answer = dis
        break

    for dir in dirs:
        nx,ny = dir[0]+cx, dir[1]+cy
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny][broken]==False and graph[nx][ny]==0:
                q.append((nx,ny,broken,dis+1))
                visited[nx][ny][broken] = True

            elif graph[nx][ny]==1 and broken==0 and visited[nx][ny][1]==False:
                q.append((nx,ny,1,dis+1))
                visited[nx][ny][1] = True

print(answer)