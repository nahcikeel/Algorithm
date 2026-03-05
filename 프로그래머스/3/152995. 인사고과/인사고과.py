def solution(scores):
    
    wanho_a = scores[0][0]
    wanho_b = scores[0][1]
    wanho_t = (wanho_a + wanho_b)
    
    scores.sort(key = lambda x : (-x[0], x[1]))
    
    max_b = -1
    rank = 1
    
    for a,b in scores:
        if b < max_b:
            if a == wanho_a and b == wanho_b:
                return -1
            continue
        max_b = max(max_b, b)
        
        if (a+b) > wanho_t:
            rank += 1
    
    return rank