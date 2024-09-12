from datetime import datetime

def solution(fees, records):
    
    basic_time = fees[0]
    basic_fee  = fees[1]
    per_min = fees[2]
    per_fee = fees[3]
    
    info = dict()
    history = []
    
    for record in records:
        time, car, io = record.split()
        
        if io == 'IN':
            history.append(car)
            if car not in info:
                info[car] = {'name': car, 'total_time': 0}
            info[car]['in_time'] = time
            
        elif io == 'OUT':
            history.remove(car)
            in_time = datetime.strptime(info[car]['in_time'],'%H:%M')
            out_time = datetime.strptime(time,'%H:%M')
            parked_time = (out_time - in_time).total_seconds() / 60
            
            info[car]['total_time'] += parked_time
    
    
    end_time = datetime.strptime('23:59', '%H:%M')
    if history:
        for h in history[:]:
            in_time = datetime.strptime(info[h]['in_time'], '%H:%M')
            parked_time = (end_time - in_time).total_seconds() / 60
            history.remove(h)
            info[h]['total_time'] += parked_time
    
    result = []
    for i in info:
        if info[i]['total_time'] <= basic_time:
            fee = basic_fee
            result.append([int(i), fee])
        
        else:
            fee = (info[i]['total_time'] - basic_time + per_min - 1) // per_min * per_fee + basic_fee
            result.append([int(i), fee])
    
    result.sort(key = lambda x:x[0])
    answer = [x[1] for x in result]
    
    return answer