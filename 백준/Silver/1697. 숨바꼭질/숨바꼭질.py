from collections import deque

max = 100001

def bfs(a,b):
    visited = [False]*max
    q = deque()
    visited[a] = True
    q.append((a,0))
    while q:
        cur, time =  q.popleft()
        if cur == b:
            return time
        
        for nxt in [cur-1, cur+1, cur*2]:
            if 0<=nxt<max and visited[nxt] == False:
                q.append((nxt,time+1))
                visited[nxt] = True

a,b = map(int, input().split())
print(bfs(a,b))