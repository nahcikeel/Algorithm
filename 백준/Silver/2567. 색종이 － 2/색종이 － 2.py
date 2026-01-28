paper = [[0]*101 for _ in range(101)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

for i in range(101):
    for j in range(101):
        if paper[i][j] == 1:
            for d in range(4):
                ni = i + dx[d]
                nj = j + dy[d]
                if ni < 0 or nj < 0 or ni >= 101 or nj >= 101:
                    answer += 1
                elif paper[ni][nj] == 0:
                    answer += 1

print(answer)
