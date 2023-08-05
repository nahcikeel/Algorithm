def solution(num_list):
    answer = 0
    
    gob = 1
    plus = 0
    
    for i in num_list:
        gob *= i
    for j in num_list:
        plus += j
    
    if gob > plus **2:
        answer = 0
    else:
        answer = 1
    
    return answer