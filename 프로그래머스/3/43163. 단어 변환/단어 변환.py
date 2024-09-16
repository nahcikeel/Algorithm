from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    
    n = len(begin)
    m = len(words)
    
    q = deque()
    q.append([begin, 0])

    while q:
        now, cnt = q.popleft()
        
        if now == target:
            answer = cnt
            break
            
        for i in range(m):
            temp_cnt = 0
            
            for j in range(n):
                if now[j] != words[i][j]:
                    temp_cnt += 1
            
            if temp_cnt == 1:
                q.append([words[i], cnt+1])
                
    
    return answer