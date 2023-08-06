def solution(myString, pat):
    answer = list()
    ans = 0
    
    for i in myString:
        if i == 'A':
            answer.append('B')
        else:
            answer.append('A')
            
    ppp = ''.join(answer)
    
    if pat in ppp:
        ans = 1
    else:
        ans = 0
    
    return ans