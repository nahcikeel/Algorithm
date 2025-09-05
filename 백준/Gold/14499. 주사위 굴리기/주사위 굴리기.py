
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

dice = [0]*6


dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

top, north, east, west, south, bottom = 0,1,2,3,4,5

def roll(d):
    global dice
    t,n,e,w,s,b = dice
    if d==1:
        dice[top], dice[east], dice[bottom], dice[west] = w, t, e, b
    elif d==2:
        dice[top], dice[east], dice[bottom], dice[west] = e, b, w, t
    elif d==3:
        dice[top], dice[north], dice[bottom], dice[south] = s, t, n, b
    elif d==4:
        dice[top], dice[north], dice[bottom], dice[south] = n, b, s, t

r,c = x,y

for d in commands:
    nr,nc = r+dr[d], c+dc[d]
    if not (0<=nr<n and 0<=nc<m):
        continue

    roll(d)

    if board[nr][nc]==0:
        board[nr][nc] = dice[bottom]
    else:
        dice[bottom] = board[nr][nc]
        board[nr][nc] = 0

    print(dice[top])
    r,c = nr,nc
