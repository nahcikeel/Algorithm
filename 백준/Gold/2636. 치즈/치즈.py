from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dirs = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs():
    q = deque([(0,0)])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    melted = []

    while q:
        cx,cy = q.popleft()
        for dx,dy in dirs:
            nx = dx + cx
            ny = dy + cy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 1:
                    melted.append((nx,ny))
                elif graph[nx][ny] == 0:
                    q.append((nx,ny))
    return melted

day = 0
cnt = 0

while True:
    melted = bfs()

    if not melted:
        break

    day += 1
    cnt = len(melted)
    for x,y in melted:
        graph[x][y] = 0

print(day)
print(cnt)