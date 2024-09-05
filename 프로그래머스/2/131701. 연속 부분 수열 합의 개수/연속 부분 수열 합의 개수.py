from collections import deque

def solution(elements):
    
    answer = []
    q = deque(elements)
    
    for i in range(len(q)):
        sum = 0
        
        for e in q:
            sum += e
            answer.append(sum)
        q.append(q.popleft())
    
    answer = list(set(answer))
        
    return len(answer)