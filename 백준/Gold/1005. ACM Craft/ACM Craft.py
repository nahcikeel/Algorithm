from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n,k = map(int, input().split())
    time = [0]+list(map(int, input().split()))
    
    graph = [[] for _ in range(n+1)]
    indegree = [0]*(n+1)

    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1
    
    w = int(input())
    
    dp = time[:]
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            dp[nxt] = max(dp[nxt], dp[cur]+time[nxt])
            indegree[nxt] -= 1
            if indegree[nxt]==0:
                    q.append(nxt)
    print(dp[w])