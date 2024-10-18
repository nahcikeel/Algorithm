from collections import deque

n,m = map(int, input().split())

visited = [[0]*n for _ in range(m)]

farm = []
for _ in range(m):
    farm.append(list(map(int,input().split())))

riped = deque()

for i in range(m):
    for j in range(n):
        if farm[i][j] == 1:
            riped.append([i,j])
        elif farm[i][j] == -1:
            visited[i][j] = 1

x = [-1,1,0,0]
y = [0,0,-1,1]

day = 0

while riped:
    

    size = len(riped)

    for _ in range(size):
        row,col = riped.popleft()
        visited[row][col] = 1

        for k in range(4):
            next_row = row + x[k]
            next_col = col + y[k]

            if (0<=next_row < m) and (0<=next_col < n) and (visited[next_row][next_col] == 0) and (farm[next_row][next_col] == 0):
                farm[next_row][next_col] = 1
                riped.append([next_row, next_col])
                visited[next_row][next_col] = 1

    if riped:
        day += 1
        
for i in range(m):
    for j in range(n):
        if farm[i][j] == 0:
            day = -1

print(day)