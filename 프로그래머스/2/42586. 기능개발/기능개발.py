def solution(progresses, speeds):
    answer = []
    
    remains = []
    for i in range(len(progresses)):
        progress = progresses[i]
        speed = speeds[i]
        if (100-progress)%speed == 0:
            remain = (100-progress)//speed
        else:
            remain = (100-progress)//speed + 1
        remains.append(remain)
    
    cnt = 1
    cur = remains.pop(0)
    while remains:
        nxt = remains.pop(0)
        
        if nxt <= cur:
            cnt += 1
            if not remains:
                answer.append(cnt)
            
        else:
            cur = nxt
            answer.append(cnt)
            cnt = 1
            if not remains:
                answer.append(cnt)
    
    return answer