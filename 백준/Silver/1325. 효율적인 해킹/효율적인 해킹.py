import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(start):
    visited = [False]*(n+1)
    q = deque([start])
    visited[start] = True
    cnt = 1
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)
    return cnt

max_hack = 0
answer = []
for i in range(1, n+1):
    c = bfs(i)
    if c > max_hack:
        max_hack = c
        answer = [i]
    elif c == max_hack:
        answer.append(i)

print(*answer)
