def HtoM(time1):
    h,m = map(int, time1.split(':'))
    return h*60 + m

def MtoH(time2):
    h = time2//60
    m = time2%60
    return f'{h:02d}:{m:02d}'

def solution(n, t, m, timetable):
    
    timetable = [HtoM(t) for t in timetable]
    timetable.sort()
    
    bus1 = HtoM('09:00')
    buses = [bus1 + t*i for i in range(n)]
    
    idx = 0
    for bus in buses:
        cnt = 0
        while idx < len(timetable) and timetable[idx] <= bus and cnt < m:
            idx += 1
            cnt += 1
    
    last_bus = buses[-1]
    
    # 마지막 버스에 자리가 남았다면
    if cnt < m:
        return MtoH(last_bus)
    
    # 마지막 버스에도 자리가 없으면
    # idx -> 마지막 버스에 탑승한 사람을 가리키는 중
    else:
        return MtoH(timetable[idx-1]-1)