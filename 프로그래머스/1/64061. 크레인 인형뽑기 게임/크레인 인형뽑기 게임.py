def solution(board, moves):
    answer = 0
    bucket = []
    crain = []
    
    for i in range(len(board)):
        c = []
        for b in board:
            if b[i] != 0:
                c.append(b[i])
        crain.append(c)
    
    for m in moves:
        if len(crain[m-1]) > 0:
            # bucket.append(crain[m-1].pop(0))
            a = crain[m-1].pop(0)
            
            if len(bucket)>0 and bucket[-1] == a:
                bucket.pop()
                answer += 2
            
            else:
                bucket.append(a)

    
    return answer