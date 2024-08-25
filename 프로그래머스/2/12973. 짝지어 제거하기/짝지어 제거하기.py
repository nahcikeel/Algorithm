def solution(s):
    answer = 1
    stack = []
    
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack) > 0:
        answer = 0
    
    
    
    return answer