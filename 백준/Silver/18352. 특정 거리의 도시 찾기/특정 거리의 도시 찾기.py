import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
graph =[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1))

import heapq

INF = 1e9

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        cur_dist, cur = heapq.heappop(hq)
        
        if cur_dist > dist[cur]:
            continue
        
        for nxt, cost in graph[cur]:
            new_dist = cur_dist + 1
            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(hq, (new_dist, nxt))
                
    return dist

dist = dijkstra(x)

found = False

for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        found = True
if not found:
    print(-1)