from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    visited = [False] * n
    q = deque([i])
    
    while q:
        now = q.popleft()
        for next in range(n):
            if graph[now][next] == 1 and not visited[next]:
                visited[next] = True
                q.append(next)
    
    for j in range(n):
        if visited[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
