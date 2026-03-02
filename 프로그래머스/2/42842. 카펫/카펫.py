def solution(brown, yellow):
    
    width  = 0  # 가로
    height = 0  # 세로
    dimension = brown + yellow  # 넓이

    
    for i in range(3,int(dimension**0.5)+1):
        if dimension % i == 0:
            width  = max(dimension//i, i)
            height = min(dimension//i, i)
            
            if width*2 + (height-2)*2 == brown:
                return [width,height]
            
    
    