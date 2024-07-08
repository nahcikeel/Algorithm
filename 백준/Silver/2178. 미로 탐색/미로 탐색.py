import sys
from collections import deque

# input = sys.stdin.readline

n, m = map(int, input().split())
miro = []

for _ in range(n):
    miro.append(list(map(int, input().rstrip())))
    
visited = [[0] * m for _ in range(n)]
q = deque()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

q.append([0,0])

while q:
    cxy = q.popleft()

    for i in range(4):

        cx = dx[i] + cxy[0]
        cy = dy[i] + cxy[1]

        if (cx>=0) & (cy>=0) & (cx<n) & (cy<m):
            if (miro[cx][cy]==1) & (visited[cx][cy]==0):
                miro[cx][cy] = miro[cxy[0]][cxy[1]] + 1
                q.append([cx,cy])
                visited[cx][cy] = 1

print(miro[n-1][m-1])