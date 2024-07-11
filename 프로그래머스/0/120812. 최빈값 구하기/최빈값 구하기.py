def solution(array):
    answer = 0
    
    a = [0]*(1001)
    
    for i in array:
        a[i] += 1
    
    b = max(a)
    
    if a.count(b) > 1:
        return -1

    answer = a.index(b)
    
    return answer