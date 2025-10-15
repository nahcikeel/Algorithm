n = int(input())
a,b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

from collections import deque

def bfs(start, end):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])

    while q:
        cur = q.popleft()

        if cur == end:
            return visited[end]
        
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)

result = bfs(a,b)
print(-1 if result is None else result)