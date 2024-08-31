def solution(s):
    
    answer = 0
    turn = 0
    
    
    while len(s)>1:
        result = ''
        turn += 1
        
        for i in s:
            if i != '0':
                result += i
            else:
                answer += 1
        
        s = bin(len(result))[2:]
    
    return [turn,answer]