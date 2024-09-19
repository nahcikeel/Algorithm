def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    a_idx = 0
    for b in B:
        if b > A[a_idx]:
            answer += 1
            a_idx += 1
            
    return answer