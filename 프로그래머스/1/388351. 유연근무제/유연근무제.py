def convertTime(time):
    h = time // 100
    m = time % 100
    return h*60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        cnt = 0
        today = startday
        
        limit = convertTime(schedules[i]) + 10
        for time in timelogs[i]:
            if (today == 6) or (today == 7):
                today += 1
                if today == 8:
                    today = 1
                continue
            
            t = convertTime(time)
            if t > limit:
                break
                
            today += 1
            
        else:
            answer += 1
            
            
            
    return answer