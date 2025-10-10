n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

max_size = 1

for i in range(n):
    for j in range(m):
        for k in range(1, min(n, m)):
            if i + k < n and j + k < m:
                if graph[i][j] == graph[i][j+k] == graph[i+k][j] == graph[i+k][j+k]:
                    max_size = max(max_size, (k+1)**2)

print(max_size)