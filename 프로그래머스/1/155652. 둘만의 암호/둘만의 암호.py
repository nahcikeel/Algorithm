def solution(s, skip, index):
    alphabet = [chr(i) for i in range(97, 123) if chr(i) not in skip]
    answer = ''
    
    for c in s:
        i = alphabet.index(c)
        new_c = alphabet[(i + index) % len(alphabet)]
        answer += new_c
    
    return answer
