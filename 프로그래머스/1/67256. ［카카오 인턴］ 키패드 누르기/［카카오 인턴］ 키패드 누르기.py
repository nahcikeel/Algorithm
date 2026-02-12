def distance(start,end):
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == start:
                sx,sy = i,j
            if keypad[i][j] == end:
                ex, ey = i,j
    return abs(sx-ex) + abs(sy-ey)
                
    
def solution(numbers, hand):
    answer = ''
    
    left_hand = '*'
    right_hand = '#'
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_hand = num

        elif num in [3,6,9]:
            answer += 'R'
            right_hand = num
            
        else:
            l_dis = distance(left_hand, num)
            r_dis = distance(right_hand, num)
            
            if r_dis > l_dis:
                answer += 'L'
                left_hand = num
            elif r_dis < l_dis:
                answer += 'R'
                right_hand = num
            else:
                if hand == 'right':
                    answer += 'R'
                    right_hand = num
                else:
                    answer += 'L'
                    left_hand = num
        
    return answer