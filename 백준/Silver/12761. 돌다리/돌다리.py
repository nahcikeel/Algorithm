from collections import deque

def bfs(n):
    q = deque()
    q.append(n)

    visited[n] = 1
    distance[n] = 0

    while q:
        visit = q.popleft()

        if visit == m:
            return distance[visit]
        
        for i in [visit+1, visit-1, visit+a, visit-a, visit+b, visit-b, visit*a, visit*b]:
            if 0<= i <= 100000 and visited[i] == -1:
                visited[i] = 1
                distance[i] = distance[visit] + 1
                q.append(i)

a,b,n,m = map(int, input().split())

visited = [-1]*100001     # 0~100000
distance = [0]*100001

answer = bfs(n)
print(answer)