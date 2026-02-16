def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x:x[1])
    last_shot = -1
    for start,end in targets:
        if last_shot < start:
            last_shot = end-1
            answer += 1
    
    return answer