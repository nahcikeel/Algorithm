def solution(n,a,b):
    answer = 1
    
    if (abs(a-b)==1) and (min(a,b)%2==1) and (max(a,b)%2==0):
        return answer

    while n > 1:
        
        answer += 1
        
        if a%2==0:
            a = a//2
        else:
            a = (a//2 + 1)
        
        if b%2==0:
            b = b//2
        else:
            b = b//2+1
        
        n = n//2
        
        if (abs(a-b)==1) and (min(a,b)%2==1) and (max(a,b)%2==0):
            break
        
    return answer