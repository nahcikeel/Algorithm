n, m = map(int, input().split())
floor = [input().strip() for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if floor[i][j] == '-':
            if j == 0 or floor[i][j-1] != '-':
                count += 1
        else:
            if i == 0 or floor[i-1][j] != '|':
                count += 1

print(count)
