def solution(str_list, ex):
    answer = list()
    
    for i in str_list:
        if ex not in i:
            answer.append(i)
            
    a = ''.join(answer)
    
    
    
    return a