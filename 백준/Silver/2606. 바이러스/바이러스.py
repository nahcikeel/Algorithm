from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque([x])
    cnt = 0
    visited = [0] * (n + 1)
    visited[x - 1] = 1 

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node - 1]:  
                visited[next_node - 1] = 1
                q.append(next_node)
                cnt += 1

    return cnt

print(bfs(1))