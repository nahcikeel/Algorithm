def convert(melody):
    change = {'C#': 'c', 'D#': 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a', 'B#':'b'}
    for k,v in change.items():
        melody = melody.replace(k,v)
    return melody

def StoM(start, end):
    eh,em = map(int, end.split(':'))
    sh,sm = map(int, start.split(':'))
    return (eh*60+em) - (sh*60+sm)
    
def full_melody(melody, play_time):
    result = ''
    for i in range(play_time):
        result += melody[i % len(melody)]
    return result


def solution(m, musicinfos):
    answer = '(None)'
    
    max_time = 0
    m = convert(m)
    
    for music in musicinfos:
        start,end,title,melody = music.split(',')
        
        melody = convert(melody)
        play_time = StoM(start, end)
        result = full_melody(melody, play_time)
        
        if m in result:
            if play_time>max_time:
                max_time = play_time
                answer = title
                
    return answer