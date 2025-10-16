import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m,r = map(int, input().split())
    
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
        
for i in range(1,n+1):
    graph[i].sort()

visited = [False] * (n+1)
order = [0]*(n+1)
cnt = 1

def dfs(start):
    global cnt
    visited[start] = True
    order[start] = cnt
    cnt += 1

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

dfs(r)
for i in range(1, n+1):
    print(order[i])