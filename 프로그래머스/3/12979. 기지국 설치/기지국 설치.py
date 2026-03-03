def solution(n, stations, w):
    answer = 0
    cover = 2*w+1

    idx = 0
    position = 1
    
    while position <= n:
        if idx < len(stations) and position >= stations[idx] - w:
            position = stations[idx] + w + 1
            idx += 1
        
        else:
            answer += 1
            position += cover
            
    return answer