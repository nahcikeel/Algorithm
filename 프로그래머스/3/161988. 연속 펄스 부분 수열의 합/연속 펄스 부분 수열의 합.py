def solution(sequence):
    n = len(sequence)
    
    # 펄스 수열 만들기 
    pulse1 = []
    pulse2 = []
    for _ in range(n//2+1):
        pulse1.append(1)
        pulse1.append(-1)
        pulse2.append(-1)
        pulse2.append(1)
    
    arr1 = [sequence[i] * pulse1[i] for i in range(n)]
    arr2 = [sequence[i] * pulse2[i] for i in range(n)]
    
    # pulse1 부분 수열 합
    cur1 = arr1[0]
    cur_max1 = arr1[0]
    for i in arr1[1:]:
        cur1 = max(cur1+i, i)
        cur_max1 = max(cur1, cur_max1)
        
    # pulse2 부분 수열 합
    cur2 = arr2[0]
    cur_max2 = arr2[0]
    for i in arr2[1:]:
        cur2 = max(cur2+i, i)
        cur_max2 = max(cur2, cur_max2)
    
    
    
    return max(cur_max1, cur_max2)