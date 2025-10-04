from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

players = list(range(n))
min_diff = float('inf')

for team in combinations(players, n//2):
    start = set(team)
    link = set(players) - start
    
    # 스타트 팀 능력치
    start_score = 0
    for i, j in combinations(start, 2):
        start_score += s[i][j] + s[j][i]
    
    # 링크 팀 능력치
    link_score = 0
    for i, j in combinations(link, 2):
        link_score += s[i][j] + s[j][i]
    
    min_diff = min(min_diff, abs(start_score - link_score))

print(min_diff)