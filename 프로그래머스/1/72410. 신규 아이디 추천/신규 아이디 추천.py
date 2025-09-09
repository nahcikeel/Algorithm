def solution(new_id):
    
    #1
    new_id = new_id.lower()
    #2
    allowed = '0123456789abcdefghijklmnopqrstuvwxyz-_.'
    ans = ''
    for n in new_id:
        if n in allowed:
            ans += n
    #3
    new_ans = ''
    prev = ''
    for c in ans:
        if c == '.' and prev == '.':
            continue
        new_ans += c
        prev = c
    ans = new_ans
    
    #4
    if ans and ans[0]=='.':
        ans = ans[1:]
    if ans and ans[-1]=='.':
        ans = ans[:-1]
    
    #5
    if len(ans)==0:
        ans = 'a'
        
    #6
    if len(ans)>=16:
        ans = ans[:15]
        if ans[-1]=='.':
            ans = ans[:-1]
    #7
    if len(ans)<=2:
        last = ans[-1]
        while len(ans)<3:
            ans += last
    
    return ans