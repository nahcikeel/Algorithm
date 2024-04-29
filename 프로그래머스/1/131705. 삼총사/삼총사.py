def solution(number):
    answer = 0
    
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for l in range(j+1,len(number)):
                if number[i] + number[j] + number[l] == 0:
                    answer +=1
    
    
    return answer