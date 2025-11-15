import heapq

node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))


INF = 10**15
dist = [INF]*(node+1)
dist[1] = 0

hq = [(0,1)]

while hq:
    cur_cost, cur_node = heapq.heappop(hq)

    if cur_cost > dist[cur_node]:
        continue
    
    for nxt_cost, nxt_node in graph[cur_node]:
        new_cost = cur_cost + nxt_cost
        if dist[nxt_node] > new_cost:
            dist[nxt_node] = new_cost
            heapq.heappush(hq, (new_cost,nxt_node))

print(dist[node])