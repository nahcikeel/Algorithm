def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        new_array = array[start:end]
        new_array.sort()
        
        answer_index = commands[i][2] - 1
        answer.append(new_array[answer_index])
        
    
    return answer
