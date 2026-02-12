def solution(n, w, num):
    target_row = (num - 1) // w
    
    if target_row % 2 == 0:
        target_col = (num - 1) % w
    else:
        target_col = w - 1 - ((num - 1) % w)
    
    answer = 0
    
    row = target_row
    
    while True:
        
        if row % 2 == 0:
            box_number = row * w + target_col + 1
        else:
            box_number = row * w + (w - target_col)
        
        if box_number > n:
            break
        
        answer += 1
        row += 1
        
    return answer
