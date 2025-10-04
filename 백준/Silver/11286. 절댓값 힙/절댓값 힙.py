import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap: 
            _, ans = heapq.heappop(heap)
            print(ans)
        else:
            print(0)