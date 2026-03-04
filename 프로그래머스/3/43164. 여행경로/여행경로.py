from collections import defaultdict

def solution(tickets):
    
    airlines = defaultdict(list)
    for s,e in sorted(tickets):
        airlines[s].append(e)
    
    route = []
    
    def dfs(airport):
        while airlines[airport]:
            dfs(airlines[airport].pop(0))
        route.append(airport)
    
    dfs("ICN")
    return route[::-1]