def solution(brown, yellow):

    square = brown+yellow  # 총면적
    
    for height in range(3,square):
        if square%height==0:
            width = square//height
            
            if (width-2)*(height-2) == yellow:
                return [width,height]
    