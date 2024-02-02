def solution(s):
    answer = ''
    
    a = int(len(s)/2)
    
    if len(s)%2:    # 홀수길이 
        answer = s[a]
    else:    # 짝수길이
        answer = s[a-1:a+1]
    
    return answer