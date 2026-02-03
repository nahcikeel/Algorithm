from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    
    for c in counter:
        if counter[c] >= 2:
            answer += counter[c] * (counter[c]-1) // 2
    
    ratios = [(2,3), (2,4), (3,4)]
    for w in counter:
        for a,b in ratios:
            result = w*a/b
            if result.is_integer() and result in counter:
                answer += counter[w] * counter[result]
    
    return answer