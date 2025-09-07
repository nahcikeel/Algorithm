from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]

shark_r,shark_c = 0,0

for i in range(n):
    for j in range(n):
        if sea[i][j] == 9:
            shark_r, shark_c = i,j
            sea[i][j] = 0
            break

shark_size = 2
eat = 0
time = 0

def bfs(r, c, shark_size):
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    q.append((r,c))
    visited[r][c] = 0

    min_dist = None

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    fishes = []

    while q:
        r,c = q.popleft()
        d = visited[r][c]

        
        if min_dist and d > min_dist:
            break

        if 0 < sea[r][c] < shark_size:
            fishes.append((d,r,c))
            min_dist = d
            continue
        
        for i in range(4):
            nr,nc = r+dr[i], c+dc[i]
            if 0<=nr<n and 0<=nc<n and visited[nr][nc] == -1:
                if sea[nr][nc] <= shark_size:
                    visited[nr][nc] = d+1
                    q.append((nr,nc))
    if fishes:
        fishes.sort()
        return fishes[0]
    return None

while True:
    result = bfs(shark_r, shark_c, shark_size)
    if result is None:
        break
    d,nr,nc = result

    time += d
    eat += 1
    sea[nr][nc] = 0
    shark_r,shark_c = nr,nc

    if eat == shark_size:
        shark_size += 1
        eat = 0

print(time)