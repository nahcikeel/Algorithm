import sys
from collections import deque

input = sys.stdin.readline 

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

count = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
