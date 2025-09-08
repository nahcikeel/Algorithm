import sys
input = sys.stdin.readline

n = int(input().strip())
board = [[0]*101 for _ in range(101)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(n):
    x,y,d,g = map(int, input().split())

    cur = [d]
    for _ in range(g):
        cur += [(dir+1) % 4 for dir in reversed(cur)]

    board[y][x] = 1

    for dir in cur:
        x += dx[dir]
        y += dy[dir]

        if 0<=x<=100 and 0<=y<=100:
            board[y][x] = 1

ans = 0

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            ans += 1

print(ans)