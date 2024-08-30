def solution(n):
    answer = 1
    result = 0
    
    for i in range(1, n//2+1):
        result = 0
        
        for j in range(i,n+1):
            
            result += j
            
            if result == n:
                answer += 1
                break
                
            elif result > n:
                break
    
    return answer