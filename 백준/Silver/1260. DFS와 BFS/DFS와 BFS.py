n,m,v = map(int, input().split())
node = [[] for _ in range(n+1)]
for _ in range(m):
    s,e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)
    
for i in range(1, n+1):
    node[i].sort()
    
visited = [False]*(n+1)
def dfs(x, visited):
    visited[x] = True
    print(x, end=' ')
    for nxt in node[x]:
        if not visited[nxt]:
            dfs(nxt, visited)

from collections import deque

def bfs(start):
    visited = [False]*(n+1)
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for nxt in node[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

dfs(v, visited)
print()
bfs(v)