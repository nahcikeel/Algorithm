def solution(players, m, k):
    answer = 0
    server = [0]*24
    
    for i in range(24):
        remain = players[i] - (server[i]*m)
        if remain >= m:
            end = min(i+k, len(players))
            for j in range(i,end):
                server[j] += remain//m
            answer += remain//m
            
    return answer