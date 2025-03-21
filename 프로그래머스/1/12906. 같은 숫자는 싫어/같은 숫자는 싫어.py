def solution(arr):
    answer = [arr[0]]
    n = len(arr)
    
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer