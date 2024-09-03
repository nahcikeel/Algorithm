def solution(k, tangerine):
    answer = 0
    
    fruits = dict()
    
    for t in tangerine:
        if t in fruits:
            fruits[t] += 1
        else:
            fruits[t] = 1
            
    sorted_fruits = sorted(fruits.values(), reverse = True)
            
    for f in sorted_fruits:
        k -= f
        answer += 1
        if k <= 0:
            break

    
    return answer