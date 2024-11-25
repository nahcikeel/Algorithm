def calculate_total(diff,time,time_prev,level):
    if diff<=level:
        return time
    else:
        return (diff-level)*(time_prev+time) + time
        
        
def solution(diffs, times, limit):
    
    n = len(diffs)
    min_level, max_level = 1, max(diffs)
    
    while (min_level<max_level):
        level = (min_level+max_level)//2
        total = 0
        
        for i in range(n):
            if i==0:
                total = times[0]
            else:
                diff = diffs[i]
                time = times[i]
                
                total += calculate_total(diff,time, times[i-1], level)
                
            if total>limit:
                break
        
        if total>limit:
            min_level = level+1
        else:
            max_level = level
            
    return min_level