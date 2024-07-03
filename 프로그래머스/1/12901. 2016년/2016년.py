import datetime

def solution(a, b):
    answer = ''
    
    weekdays = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    find_day = datetime.datetime(2016, a, b).weekday()
    
    return weekdays[find_day]