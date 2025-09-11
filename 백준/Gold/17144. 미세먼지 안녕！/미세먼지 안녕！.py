import sys
input = sys.stdin.readline

r,c,t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if room[i][0] == -1:
        up = i
        down = i+1
        break
        
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def spread():
    temp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if room[x][y] > 0:
                amount = room[x][y]//5
                cnt = 0
                for dir in range(4):
                    nx = dx[dir]+x
                    ny = dy[dir]+y
                    if 0<=nx<r and 0<=ny<c and room[nx][ny]!=-1:
                        temp[nx][ny] += amount
                        cnt += 1
                room[x][y] -= amount*cnt
    for i in range(r):
        for j in range(c):
            room[i][j] += temp[i][j]
def air_clean():
    for i in range(up-1,0,-1):
        room[i][0] = room[i-1][0]
    for j in range(c-1):
        room[0][j] = room[0][j+1]
    for i in range(up):
        room[i][c-1] = room[i+1][c-1]
    for j in range(c-1, 1, -1):
        room[up][j] = room[up][j-1]
    room[up][1] = 0

    for i in range(down+1, r-1):
        room[i][0] = room[i+1][0]
    for j in range(c-1):
        room[r-1][j] = room[r-1][j+1]
    for i in range(r-1, down, -1):
        room[i][c-1] = room[i-1][c-1]
    for j in range(c-1, 1, -1):
        room[down][j] = room[down][j-1]
    room[down][1] = 0

for _ in range(t):
    spread()
    air_clean()

ans = 0
for i in range(r):
    for j in range(c):
        if room[i][j]>0:
            ans += room[i][j]
print(ans)