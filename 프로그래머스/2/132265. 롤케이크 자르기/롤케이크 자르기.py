def solution(topping):
    answer = 0
    n = len(topping)
    right_dict = dict()
    left_cnt = set()
    
    for i in range(n):
        if topping[i] in right_dict:
            right_dict[topping[i]] += 1
        else:
            right_dict[topping[i]] = 1
            
    for j in range(n):
        left_cnt.add(topping[j])
        
        if right_dict[topping[j]] == 1:
            del right_dict[topping[j]]
            
        else:
            right_dict[topping[j]] -= 1
            
        if len(left_cnt) == len(right_dict):
            answer += 1
    
    return answer