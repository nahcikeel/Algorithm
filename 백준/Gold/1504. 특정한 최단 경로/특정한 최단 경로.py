import heapq

n,e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a,b,k = map(int, input().split())
    graph[a].append((b,k))
    graph[b].append((a,k))

v1, v2 = map(int, input().split())

INF = 1e9

def dijkstra(start):
    dist = [INF] *(n+1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        cur_cost, cur = heapq.heappop(hq)

        if dist[cur] < cur_cost:
            continue
        
        for nxt, cost in graph[cur]:
            new_cost = cur_cost + cost
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(hq, (new_cost, nxt))

    return dist

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[n]
path2 = dist1[v2] + dist_v2[v1] + dist_v1[n]

result = min(path1, path2)
print(result if result < INF else -1)