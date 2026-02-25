from collections import deque

n,k = map(int, input().split())
max_num = 100001

dist = [-1] * max_num
dist[n] = 0

q = deque()
q.append(n)

while q:
    x = q.popleft()
    if x == k:
        print(dist[x])
        break

    nx = x*2
    if (0 <= nx < max_num) and dist[nx] == -1:
        dist[nx] = dist[x]
        q.appendleft(nx)
    
    for nx in (x-1,x+1):
        if (0 <= nx < max_num) and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)