import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

start, end = map(int, input().split())

INF = 0
max_w = [0]*(n+1)
max_w[start] = float('inf')

hq = [(-max_w[start], start)]

while hq:
    cur_w, cur_node = heapq.heappop(hq)
    cur_w = -cur_w

    if max_w[cur_node] > cur_w:
        continue

    for nxt_w, nxt_node in graph[cur_node]:
        path_w = min(cur_w, nxt_w)
        if max_w[nxt_node] < path_w:
            max_w[nxt_node] = path_w
            heapq.heappush(hq, (-path_w, nxt_node))

print(max_w[end])
