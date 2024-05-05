def solution(s):
    answer = []
    alp_idx = {}
    
    for idx, alp in enumerate(s):
        if alp not in alp_idx:
            answer.append(-1)
        else:
            answer.append(idx - alp_idx[alp])
            
        alp_idx[alp] = idx
    
    return answer
    
    
    
    
    return answer