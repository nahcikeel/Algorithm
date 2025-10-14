import heapq
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,k = map(int, input().split())
    graph[a].append((b,k))
s,e = map(int, input().split())

import heapq

INF = 1e9

def dijkstra(start, end):
    hq = [(0, start)]
    dist = [INF] * (n+1)
    dist[start] = 0

    while hq:
        cur_cost, cur = heapq.heappop(hq)

        if dist[cur] < cur_cost:
            continue
        
        for nxt, cost in graph[cur]:
            new_cost = cur_cost + cost
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(hq, (new_cost, nxt))
    
    return dist[end]

print(dijkstra(s,e))