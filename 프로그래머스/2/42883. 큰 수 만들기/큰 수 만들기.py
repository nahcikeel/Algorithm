def solution(number, k):
    n = len(number)
    answer = []
    
    for num in number:
        while answer and k>0 and answer[-1]<num:
            answer.pop()
            k -= 1
        answer.append(num)
    
    answer = ''.join(answer)
    answer = answer[:n-k]
    
    return answer