from collections import deque

def solution(order):
    cnt = 0
    n = len(order)
    boxes = deque([i for i in range(1, n+1)])
    assist = deque()
    now = 0
    
    while boxes or assist:
        if assist and assist[-1] == order[now]:
            cnt += 1
            now += 1
            assist.pop()
        
        elif boxes and boxes[0] == order[now]:
            cnt += 1
            now += 1
            boxes.popleft()
        
        elif boxes:
            assist.append(boxes.popleft())
        
        else:
            break
    
    return cnt