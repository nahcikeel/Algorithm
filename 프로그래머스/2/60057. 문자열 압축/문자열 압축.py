def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2+1):
        compressed = ''
        prev = s[0:step]
        count = 1
        
        for i in range(step,len(s), step):
            cur = s[i:i+step]
            
            if cur == prev:
                count += 1
            else:
                if count>1:
                    compressed += str(count)
                compressed += prev
                prev = cur
                count = 1
            
        if count>1:
            compressed += str(count)
        compressed += cur
        
        answer = min(answer, len(compressed))
    
    return answer