def solution(n, s):
    answer = []
    
    if s<n:
        return [-1]

    i = s // n
    j = s %  n

    answer = [i]*n

    for k in range(j):
        answer[-(k+1)] += 1

    return answer