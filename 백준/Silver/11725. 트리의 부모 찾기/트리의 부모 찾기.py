import sys
from collections import deque

def find_parents():
    input = sys.stdin.readline
    n = int(input())

    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    parents = [0] * (n+1)

    q = deque([1])  
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if parents[nxt] == 0 and nxt != 1:
                parents[nxt] = cur
                q.append(nxt)

    for i in range(2, n+1):
        print(parents[i])

find_parents()
