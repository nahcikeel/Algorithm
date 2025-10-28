def solution(a, b, g, s, w, t):
    answer = -1
    
    left = 0
    right = 10**15
    
    while left <= right:
        mid = (left+right)//2
        
        total_gold = 0
        total_silver = 0
        total_sum = 0
        
        for i in range(len(g)):
            cnt = mid // (2*t[i])
            if mid%(2*t[i]) >= t[i]:
                cnt += 1
            move = cnt*w[i]
            
            total_gold   += min(g[i], move)
            total_silver += min(s[i], move)
            total_sum    += min(g[i]+s[i], move)
    
        if total_gold>=a and total_silver>=b and total_sum>=(a+b):
            answer = mid
            right = mid-1
        else:
            left = mid+1
    
    return answer