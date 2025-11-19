n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dirs = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]

visited = [[False] * n for _ in range(n)]

def can_place(x, y):
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if visited[nx][ny]:
            return False
    return True

def place_flower(x, y, flag):
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        visited[nx][ny] = flag

def cost(x, y):
    s = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        s += board[nx][ny]
    return s

answer = float('inf')

def dfs(cnt, total):
    global answer

    if cnt == 3:
        answer = min(answer, total)
        return

    for i in range(1, n-1):
        for j in range(1, n-1):
            if can_place(i, j):
                c = cost(i, j)
                place_flower(i, j, True)
                dfs(cnt+1, total + c)
                place_flower(i, j, False)

dfs(0, 0)
print(answer)
