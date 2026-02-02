def solution(storey):
    click = 0
    
    while storey>0:
        digit = storey%10
        
        # 올림
        if digit > 5:
            click += 10-digit
            storey += 10
        
        # 내림
        elif digit < 5:
            click += digit
        
        # 다음 자리보고 결정
        else:
            if (storey//10)%10 >= 5:
                click += 5
                storey += 10
            else:
                click += 5
        
        storey //= 10
    
    return click