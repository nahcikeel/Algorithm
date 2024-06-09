def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name,yearning))
    
    for people in photo:
        result = 0
        for person in people:
            if person in name:
                result += dic[person]
        answer.append(result)
    
    return answer