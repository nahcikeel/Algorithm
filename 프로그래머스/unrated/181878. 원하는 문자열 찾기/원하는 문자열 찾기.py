def solution(myString, pat):
    answer = 0
    
    b = myString.lower()
    a = pat.lower()
    
    if a in b:
        answer = 1
    
    return answer