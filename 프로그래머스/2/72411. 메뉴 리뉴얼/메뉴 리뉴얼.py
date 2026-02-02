from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for k in course:
        counter = Counter()
        
        for order in orders:
            order = sorted(order)
            for comb in combinations(order, k):
                counter[''.join(comb)] += 1
            
        if not counter:
            continue
            
        max_cnt = max(counter.values())
        if max_cnt < 2:
            continue
            
        for menu,cnt in counter.items():
            if cnt == max_cnt:
                answer.append(menu)
    
    return sorted(answer)