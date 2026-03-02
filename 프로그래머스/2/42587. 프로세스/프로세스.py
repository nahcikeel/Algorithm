from collections import deque

def solution(priorities, location):

    q = deque()
    for idx,num in enumerate(priorities):
        q.append((idx,num))
    
    cnt = 0
    while q:
        idx,num = q.popleft()
        if num == max(priorities):
            priorities.remove(num)
            cnt += 1
            if idx == location:
                break
        else:
            q.append(((idx,num)))
                
    return cnt