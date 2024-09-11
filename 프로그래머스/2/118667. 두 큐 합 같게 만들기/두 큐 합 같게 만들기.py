from collections import deque

def solution(queue1, queue2):
    cnt = 0
    
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    max_try = len(queue1)*3

    while cnt < max_try:
        
        if sum_q1 == sum_q2:
            return cnt
        
        elif sum_q1 > sum_q2:
            v1 = queue1.popleft()
            queue2.append(v1)
            
            sum_q1 -= v1
            sum_q2 += v1
            cnt += 1
        
        else:
            v2 = queue2.popleft()
            queue1.append(v2)
            
            sum_q1 += v2
            sum_q2 -= v2
            cnt += 1
    
    return -1