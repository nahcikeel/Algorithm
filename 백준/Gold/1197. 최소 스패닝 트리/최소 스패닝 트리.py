v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

visited = [False] * (v+1)
heap = [(0,1)]
result = 0

import heapq

while heap:
    cost,node = heapq.heappop(heap)
    if visited[node]:
        continue
    visited[node] = True
    result += cost
    for nc, nn in graph[node]:
        if not visited[nn]:
            heapq.heappush(heap, (nc,nn))

print(result)