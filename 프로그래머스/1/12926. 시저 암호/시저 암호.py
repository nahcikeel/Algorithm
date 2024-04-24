def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += ' '
        elif 'a'<=i<='z':
            new_word = chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            answer += new_word
        elif 'A'<=i<='Z': 
            new_word = chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            answer += new_word
    
    return answer