def HtoM(time1):
    h,m = map(int, time1.split(':'))
    return h*60+m

def MtoH(time2):
    h = time2//60
    m = time2%60
    return f'{h:02d}:{m:02d}'

def solution(n, t, m, timetable):
    
    # 사람들 시간변환
    timetable = [HtoM(t) for t in timetable]
    timetable.sort()
    
    # 버스 시간변환
    bus1 = HtoM('09:00')
    buses = [bus1 + t*i for i in range(n)]
    
    # 처리
    idx = 0
    for bus in buses:
        cnt = 0
        
        while idx < len(timetable) and cnt < m and bus >= timetable[idx]:
            cnt += 1
            idx += 1
    
    last_bus = buses[-1]
    if cnt < m:
        return MtoH(last_bus)
    
    return MtoH(timetable[idx-1]-1)