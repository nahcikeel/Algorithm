import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            house.append((i,j))
        if graph[i][j]==2:
            chicken.append((i,j))

result = float('inf')
            
for comb in combinations(chicken, m):
    total = 0
    for hx, hy in house:
        distances = []
        for cx, cy in comb:
            distances.append(abs(hx-cx) + abs(hy-cy))
        dist = min(distances)
        total += dist

    result = min(result, total)
        
print(result)