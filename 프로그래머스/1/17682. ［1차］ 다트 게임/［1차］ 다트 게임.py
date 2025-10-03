def solution(dartResult):
    n = len(dartResult)
    idx = 0
    scores = []
    
    while idx<n:
        # 숫자 처리
        if dartResult[idx] == '1' and idx+1 < n and dartResult[idx+1] == '0':
            num = 10
            idx += 2
        else:
            num = int(dartResult[idx])
            idx += 1
        
        # 보너스 문자 처리
        bonus = dartResult[idx]
        if dartResult[idx] == 'S':
            num = num**1
            
        elif dartResult[idx] == 'D':
            num = num**2
            
        elif dartResult[idx] == 'T':
            num = num**3
        idx += 1
            
        # 옵션 처리
        if idx < n and dartResult[idx] in ['*', '#']:
            opt = dartResult[idx]
            if opt == '*':
                num *= 2
                if scores:
                    scores[-1] *= 2

            elif opt == '#':
                num *= -1
            
            idx += 1
        
        scores.append(num)

    return sum(scores)