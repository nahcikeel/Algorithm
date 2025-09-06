from itertools import combinations
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_safe = 0


for walls in combinations(empty, 3):
    tmp_lab = [row[:] for row in lab]
    for x, y in walls:
        tmp_lab[x][y] = 1

    q = deque(virus)
    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < N and 0 <= ny < M and tmp_lab[nx][ny] == 0:
                tmp_lab[nx][ny] = 2
                q.append((nx, ny))

    safe = sum(row.count(0) for row in tmp_lab)
    max_safe = max(max_safe, safe)

print(max_safe)
