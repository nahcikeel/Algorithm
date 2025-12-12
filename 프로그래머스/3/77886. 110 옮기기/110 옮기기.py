def solution(s):
    answer = []

    for string in s:
        stack = []
        cnt110 = 0
        
        for ch in string:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                cnt110 += 1
                stack.pop()
                stack.pop()
                stack.pop()

        rest = ''.join(stack)
        idx = rest.rfind('0')

        if idx == -1:
            new_str = '110' * cnt110 + rest
        else:
            new_str = rest[:idx+1] + ('110' * cnt110) + rest[idx+1:]
        
        answer.append(new_str)

    return answer
