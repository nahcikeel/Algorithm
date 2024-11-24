def min2sec(video_len):
    minute, second = map(int, video_len.split(':'))
    total = (minute*60)+second
    return total

def solution(video_len, pos, op_start, op_end, commands):
    
    video_len = min2sec(video_len)
    pos       = min2sec(pos)
    op_start  = min2sec(op_start)
    op_end    = min2sec(op_end)

    for com in commands:
        if op_start<=pos<=op_end:
            pos = op_end
        
        if com == 'next':
            if (pos+10)>video_len:
                pos = video_len
            else:
                pos += 10
        
        elif com == 'prev':
            if (pos-10)<0:
                pos = 0
            else:
                pos -= 10
                
        if op_start<=pos<=op_end:
            pos = op_end
    
    ans_min = str(pos // 60)
    ans_sec = str(pos % 60)
    
    if len(ans_min)==1:
        ans_min = '0'+ans_min
    if len(ans_sec)==1:
        ans_sec = '0'+ans_sec
    
    answer = (ans_min + ':' + ans_sec)
    
    
    return answer