from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [-1] * (n+1)
    visited[start] = 0
    q = deque([start])

    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                q.append(nxt)
    
    return sum(visited[1:])
                
min_sum = float('inf')
answer = 0

for i in range(1,n+1):
    total = bfs(i)
    if total < min_sum:
        min_sum = total
        answer = i

print(answer)