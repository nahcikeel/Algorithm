from collections import deque

SIZE = 501

board = [[0] * SIZE for _ in range(SIZE)]

n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] = 1

m = int(input())
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] = 2

INF = 10**9
dist = [[INF] * SIZE for _ in range(SIZE)]
dist[0][0] = 0

dirs = [(1,0), (-1,0), (0,1), (0,-1)]
q = deque([(0, 0)])

while q:
    cx, cy = q.popleft()
    for dx, dy in dirs:
        nx, ny = cx + dx, cy + dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE and board[nx][ny] != 2:
            cost = board[nx][ny]
            if dist[nx][ny] > dist[cx][cy] + cost:
                dist[nx][ny] = dist[cx][cy] + cost
                if cost == 1:
                    q.append((nx, ny))
                else:
                    q.appendleft((nx, ny))

ans = dist[500][500]
print(ans if ans != INF else -1)
