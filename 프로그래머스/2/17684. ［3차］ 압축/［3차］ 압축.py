def solution(msg):
    answer = []
    alpha = dict()
    
    # 사전 만들기
    for i in range(1,27):
        alpha[chr(64+i)] = i
    
    # LZW
    word = ''
    value = 26
    
    i = 0
    while i < len(msg):
        word += msg[i]
        
        if word not in alpha:
            value += 1
            alpha[word] = value
            answer.append(alpha[word[:-1]])
            word = word[-1]
        
        i += 1
        
    answer.append(alpha[word])
        
    return answer
       
