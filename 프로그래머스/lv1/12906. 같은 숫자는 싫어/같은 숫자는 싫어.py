def solution(arr):
    answer = []                        # 정답이 들어갈 리스트
    answer.append(arr[0])              # 0번째 숫자는 무조건 포함
    
    for i in range(1,len(arr)):        # 1번째 숫자부터 마지막 숫자까지 반복
        if arr[i] != arr[i-1]:         # 이전의 숫자와 다르다면 
            answer.append(arr[i])      # 정답 리스트에 추가
            
    return answer
