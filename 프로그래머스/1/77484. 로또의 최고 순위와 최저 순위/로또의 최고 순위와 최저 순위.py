def solution(lottos, win_nums):
    
    ranking = [6,6,5,4,3,2,1]
    max_win = lottos.count(0)
    
    win = 0
    for l in lottos:
        if l in win_nums:
            win += 1
    
    high = ranking[win + max_win]
    low  = ranking[win]
    
    
    
    return [high,low]