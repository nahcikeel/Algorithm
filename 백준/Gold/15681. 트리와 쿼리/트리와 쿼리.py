import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

sub = [0] * (N+1)
visited = [False] * (N+1)

def dfs(u):
    visited[u] = True
    sub[u] = 1
    for v in graph[u]:
        if not visited[v]:
            dfs(v)
            sub[u] += sub[v]

dfs(R)

out = []
for _ in range(Q):
    u = int(input())
    print(sub[u])
