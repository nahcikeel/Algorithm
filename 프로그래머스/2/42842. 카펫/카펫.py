def solution(brown, yellow):
    answer = []
    square = brown+yellow
    
    for i in range(3,square):
        if square%i==0:
            answer.append([square//i, i])
            
    for sq in answer:
        wide = sq[0]
        height = sq[1]
        
        if wide>=height:
        
            con1 = (wide-2)*(height-2)
            con2 = 2*wide + 2*height -4

            if (con1==yellow) & (con2==brown):
                ans = [wide,height]
    
    
    return ans