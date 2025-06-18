def solution(data, ext, val_ext, sort_by):
    answer = []
    df = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    for d in data:
        if d[df[ext]] < val_ext:
            answer.append(d)
    
    answer = sorted(answer, key = lambda x : x[df[sort_by]])
    
    return answer