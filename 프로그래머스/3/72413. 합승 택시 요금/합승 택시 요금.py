import heapq

INF = int(1e9)

def dijkstra(start, n, graph):

    dist = [INF] * (n+1)
    dist[start] = 0
    
    hq = [(0, start)]
    while hq:
        cost, now = heapq.heappop(hq)
        if cost > dist[now]:
            continue
        for nxt,weight in graph[now]:
            new_cost = cost + weight
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(hq, (new_cost, nxt))
    
    return dist


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for start, end, cost in fares:
        graph[start].append([end, cost])
        graph[end].append([start, cost])
    
    distS = dijkstra(s,n,graph)
    distA = dijkstra(a,n,graph)
    distB = dijkstra(b,n,graph)

    
    answer = INF
    for c in range(1, n + 1):
        answer = min(answer, distS[c] + distA[c] + distB[c])
    
    
    
    
    
    
    
    return answer