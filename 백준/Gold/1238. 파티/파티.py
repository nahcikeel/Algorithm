import heapq

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    reverse_graph[b].append((a, t))

def dijkstra(start, graph):
    INF = 1e9
    dist = [INF] * (n+1)
    dist[start] = 0
    hq = [(0, start)]

    while hq:
        cur_dist, cur = heapq.heappop(hq)

        if dist[cur] < cur_dist:
            continue
        
        for nxt, cost in graph[cur]:
            if dist[nxt] > cur_dist + cost:
                dist[nxt] = cur_dist + cost
                heapq.heappush(hq, (dist[nxt], nxt))
    return dist

to_x = dijkstra(x, graph)
from_x = dijkstra(x, reverse_graph)
max_total = 0

for i in range(1, n+1):
    total = to_x[i] + from_x[i]
    max_total = max(total, max_total)

print(max_total)