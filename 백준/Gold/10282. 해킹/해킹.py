import heapq
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n,d,c = map(int, input().split())
    computers = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int, input().split())
        computers[b].append((s,a))

    INF = 10**15
    dist = [INF] * (n+1)
    dist[c] = 0

    hq = [(0, c)]

    while hq:
        cur_dist, cur_node = heapq.heappop(hq)

        if cur_dist > dist[cur_node]:
            continue
        
        for nxt_dist, nxt_node in computers[cur_node]:
            new_dist = cur_dist + nxt_dist
            if new_dist < dist[nxt_node]:
                dist[nxt_node] = new_dist
                heapq.heappush(hq, (new_dist, nxt_node))

    infected_count = sum(1 for t in dist[1:] if t != INF)
    last_time = max([t for t in dist[1:] if t != INF])

    print(infected_count, last_time)