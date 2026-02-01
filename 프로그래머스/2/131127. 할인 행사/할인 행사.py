from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    market = dict(zip(want, number))
    
    for i in range(len(discount)-9):
        ten_days = discount[i:i+10]
        counter = Counter(ten_days)
        
        if counter == market:
            answer += 1
    
    return answer