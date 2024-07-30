def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        s.append(s.pop(0))
        q = []
        
        for i in s:
            if i==')' and q and q[-1]=='(':
                q.pop()
            elif i==']' and q and q[-1]=='[':
                q.pop()
            elif i=='}' and q and q[-1]=='{':
                q.pop()
            else:
                q.append(i)
        
        if len(q)==0:
            answer += 1
    
    return answer