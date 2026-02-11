def solution(numbers):
    answer = []
    
    for x in numbers:
        if x%2==0:
            answer.append(x+1)
            
        else:
            b = list('0'+bin(x)[2:])
            idx = ''.join(b).rfind('0')
            
            b[idx] = '1'
            b[idx+1] = '0'
            
            answer.append(int(''.join(b), 2))
    return answer