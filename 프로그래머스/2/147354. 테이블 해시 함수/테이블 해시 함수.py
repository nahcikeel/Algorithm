def solution(data, col, row_begin, row_end):
    # 1. 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    answer = 0
    
    # 2. row_begin ~ row_end
    for i in range(row_begin-1, row_end):
        row = data[i]
        idx = i + 1
        
        s = 0
        for value in row:
            s += value % idx

        answer ^= s
    
    return answer
