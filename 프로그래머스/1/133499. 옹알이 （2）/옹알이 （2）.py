def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for b in babbling:
        prev = ""
        temp = b
        
        for w in words:
            if w * 2 in temp:
                break
            temp = temp.replace(w, " ")
        else:
            if temp.strip() == "":
                answer += 1
    
    return answer
