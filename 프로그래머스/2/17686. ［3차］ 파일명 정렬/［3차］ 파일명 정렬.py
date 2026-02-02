def solution(files):
    result = []
    
    for idx, file in enumerate(files):
        head = ''
        number = ''
        i = 0
        
        while i<len(file) and not file[i].isdigit():
            head += file[i]
            i += 1
        
        while i<len(file) and file[i].isdigit():
            number += file[i]
            i += 1
        
        result.append((head,number,idx,file))
    
    result.sort(key = lambda x: (x[0].lower(), int(x[1]), x[2]))
    answer = [r[3] for r in result]
    
    return answer