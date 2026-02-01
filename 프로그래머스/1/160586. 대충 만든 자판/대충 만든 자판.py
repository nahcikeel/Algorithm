def solution(keymap, targets):
    keyboard = dict()
    
    for key in keymap:
        for idx, ch in enumerate(key, start=1):
            if ch not in keyboard:
                keyboard[ch] = idx
            else:
                keyboard[ch] = min(keyboard[ch], idx)
    
    answer = []
    for t in targets:
        total = 0
        for ch in t:
            if ch not in keyboard:
                total = -1
                break
            total += keyboard[ch]
        answer.append(total)
    
    return answer