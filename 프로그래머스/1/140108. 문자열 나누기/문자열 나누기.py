def solution(s):
    answer = 0
    i = 0
    
    while i < len(s):
        first_alp = s[i]
        s_cnt, n_cnt = 1, 0
        i += 1
        
        while i < len(s):
            if s[i] == first_alp:
                s_cnt += 1
            else:
                n_cnt += 1
            i += 1
            
            if s_cnt == n_cnt:
                break
                
        answer += 1
        
    
    return answer